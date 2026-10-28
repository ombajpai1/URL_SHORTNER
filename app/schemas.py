from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl

class ShortenRequest(BaseModel):
    url:HttpUrl
    custom_alias:Optional[str]=None
    expires_at:Optional[datetime]=None

class ShortenResponse(BaseModel):
    short_code:str
    short_url:str
    original_url:str
    expires_at:Optional[datetime]=None    
    
