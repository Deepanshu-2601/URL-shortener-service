from sqlalchemy.orm import Session
from models import URLItem
from utils import generate_short_code

# Naya short URL create karna
def create_url(db: Session, original_url: str) -> URLItem:
    # Unique code dhoondo jo DB me pehle se na ho
    short_code = generate_short_code()
    while db.query(URLItem).filter(URLItem.short_code == short_code).first():
        short_code = generate_short_code()

    db_item = URLItem(original_url=original_url, short_code=short_code)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Short code se record nikalna
def get_url_by_code(db: Session, short_code: str) -> URLItem | None:
    return db.query(URLItem).filter(URLItem.short_code == short_code).first()

# Click count +1 karna jab koi link khole
def increment_clicks(db: Session, db_item: URLItem):
    db_item.clicks += 1
    db.commit()
