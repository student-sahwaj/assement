from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

@app.post("/watchlist/")
def create_watchlist(watchlist: schemas.WatchlistCreate, db: Session = Depends(get_db)):
    return crud.create_watchlist(db, watchlist, user_id=1)  # Replace with actual user session
