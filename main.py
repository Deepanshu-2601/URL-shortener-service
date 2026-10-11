import os
os.environ["DISABLE_SQLALCHEMY_CEXT"] = "1"

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from schemas import URLCreate, URLResponse, URLStats
import crud as crud

# Database tables automatically create kar dega
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener & Analytics API",
    description="Production-grade URL shortening and click tracking service",
    version="1.0.0"
)

# 1. Health check endpoint
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "URL Shortener API is live"}

# 2. URL shorten karne ka endpoint
@app.post("/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED, tags=["URLs"])
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    url_item = crud.create_url(db=db, original_url=str(payload.original_url))
    return {
        "original_url": url_item.original_url,
        "short_code": url_item.short_code,
        "short_url": f"http://127.0.0.1:8000/{url_item.short_code}",
        "clicks": url_item.clicks,
        "created_at": url_item.created_at
    }

# 3. Analytics dekhne ka endpoint (Clicks track karne ke liye)
@app.get("/analytics/{short_code}", response_model=URLStats, tags=["Analytics"])
def get_url_analytics(short_code: str, db: Session = Depends(get_db)):
    url_item = crud.get_url_by_code(db=db, short_code=short_code)
    if not url_item:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_item

# 4. Redirect Endpoint (Short URL open karne par original URL par bhejna)
@app.get("/{short_code}", tags=["Redirect"])
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url_item = crud.get_url_by_code(db=db, short_code=short_code)
    if not url_item:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    # Click count badhao aur redirect karo
    crud.increment_clicks(db=db, db_item=url_item)
    return RedirectResponse(url=url_item.original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
