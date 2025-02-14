from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/restaurant-bonuses", tags=["restaurant_bonuses"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RestaurantBonus)
def create_restaurant_bonus(bonus: schemas.RestaurantBonusCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant_bonus(db, bonus)

@router.get("/{restaurant_bonus_id}", response_model=schemas.RestaurantBonus)
def read_restaurant_bonus(restaurant_bonus_id: int, db: Session = Depends(get_db)):
    db_bonus = crud.get_restaurant_bonus(db, restaurant_bonus_id)
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Restaurant bonus not found")
    return db_bonus