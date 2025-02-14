from sqlalchemy.orm import Session
from . import models, schemas

# Рестораны
def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def get_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.restaurant_id == restaurant_id).first()

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Restaurant).offset(skip).limit(limit).all()

# Пользователи
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Отзывы
def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.review_id == review_id).first()

def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).offset(skip).limit(limit).all()

# Бронирования
def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = models.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.reservation_id == reservation_id).first()

def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reservation).offset(skip).limit(limit).all()

# Заказы
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

# Бонусы
def create_bonus(db: Session, bonus: schemas.BonusCreate):
    db_bonus = models.Bonus(**bonus.dict())
    db.add(db_bonus)
    db.commit()
    db.refresh(db_bonus)
    return db_bonus

def get_bonus(db: Session, bonus_id: int):
    return db.query(models.Bonus).filter(models.Bonus.bonus_id == bonus_id).first()

def get_bonuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bonus).offset(skip).limit(limit).all()

# Ресторанные бонусы
def create_restaurant_bonus(db: Session, bonus: schemas.RestaurantBonusCreate):
    db_bonus = models.RestaurantBonus(**bonus.dict())
    db.add(db_bonus)
    db.commit()
    db.refresh(db_bonus)
    return db_bonus

def get_restaurant_bonus(db: Session, restaurant_bonus_id: int):
    return db.query(models.RestaurantBonus).filter(models.RestaurantBonus.restaurant_bonus_id == restaurant_bonus_id).first()

def get_restaurant_bonuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RestaurantBonus).offset(skip).limit(limit).all()

# Элементы заказа
def create_order_item(db: Session, order_item: schemas.OrderItemCreate):
    db_order_item = models.OrderItem(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

def get_order_item(db: Session, order_item_id: int):
    return db.query(models.OrderItem).filter(models.OrderItem.order_item_id == order_item_id).first()

def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()

# Погашение бонусов
def create_user_bonus_redeem(db: Session, redeem: schemas.UserBonusRedeemCreate):
    db_redeem = models.UserBonusRedeem(**redeem.dict())
    db.add(db_redeem)
    db.commit()
    db.refresh(db_redeem)
    return db_redeem

def get_user_bonus_redeem(db: Session, redeem_id: int):
    return db.query(models.UserBonusRedeem).filter(models.UserBonusRedeem.redeem_id == redeem_id).first()

def get_user_bonus_redeems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserBonusRedeem).offset(skip).limit(limit).all()
