from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.models import URLItem, KeySequence
from app.utils import encode_base62
from app.schemas import ShortenRequest

class URLService:
    def __init__(self, session:AsyncSession):
        self.session=session

    async def _get_next_id(self)->int:
        stmt=select(KeySequence).where(KeySequence.id==1).with_for_update()
        result=await self.session.execute(stmt)
        record=result.scalar_one_or_none()

        if not record:
            record=KeySequence(id=1, current_value=100000)
            self.session.add(record)
            await self.session.flush()

        record.current_value+=1
        await self.session.flush()
        return record.current_value

    async def shorten_url(self, payload:ShortenRequest)->URLItem:
        if payload.custom_alias:
            existing=await self.get_by_code(payload.custom_alias)
            
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Custom alias already in use",
                )
            else:
                next_id=await self._get_next_id()
                short_code=encode_base62(next_id)

            url_record=URLItem(
                short_code=short_code,
                original_url=str(payload.url),
                expires_at=payload.expires_at,
            )    

            self.session.add(url_record)
            await self.session.commit()
            await self.session.refresh(url_record)
            return url_record


        async def get_by_code(self, short_code:str)->Optional[URLItem]:
            stmt=select(URLItem).where(URLItem.short_code==short_code)
            result=await self.session.execute(stmt)
            return result.scalar_one_or_none()


