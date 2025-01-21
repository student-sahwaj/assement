from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_watchlist(db: Session, watchlist: schemas.WatchlistCreate, user_id: int):
    db_watchlist = models.Watchlist(**watchlist.dict(), user_id=user_id)
    db.add(db_watchlist)
    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist
