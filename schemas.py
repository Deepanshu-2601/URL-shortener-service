from datetime import datetime
from pydantic import BaseModel, HttpUrl

# User se input lene ke liye schema
class URLCreate(BaseModel):
    original_url: HttpUrl

# API response return karne ke liye schema
class URLResponse(BaseModel):
    original_url: str
    short_code: str
    short_url: str
    clicks: int
    created_at: datetime

    class Config:
        from_attributes = True

# Analytics dekhne ke liye schema
class URLStats(BaseModel):
    original_url: str
    short_code: str
    clicks: int
    created_at: datetime

    class Config:
        from_attributes = True