from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import BigInteger, DateTime,Index,String,Text, Integer
from sqlalchemy.orm import Mapped,mapped_column
from app.database import Base

class URLItem(Base):
    __tablename__="urls"

    id:Mapped[int]=mapped_column(BigInteger,primary_key=True, autoincrement=True)
    short_code:Mapped[str]=mapped_column(String(16),unique=True, index=True, nullable=False)
    original_url:Mapped[str]=mapped_column(Text,nullable=False)
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc),
        nullable=False,
    )

    expires_at:Mapped[Optional[datetime]]=mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )  


class KeySequence(Base):
    __tablename__="Key_sequence"

    id:Mapped[int]=mapped_column(Integer, primary_key=True,default=1)
    current_value:Mapped[int]=mapped_column(BigInteger,default=100000)
