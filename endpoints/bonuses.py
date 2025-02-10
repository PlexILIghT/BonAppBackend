from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/bonuses", tags=["bonuses"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Bonus)
def create_bonus(bonus: schemas.BonusCreate, db: Session = Depends(get_db)):
    return crud.create_bonus(db, bonus)

@router.get("/{bonus_id}", response_model=schemas.Bonus)
def read_bonus(bonus_id: int, db: Session = Depends(get_db)):
    db_bonus = crud.get_bonus(db, bonus_id)
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    return db_bonus