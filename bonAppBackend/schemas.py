from datetime import datetime
from pydantic import BaseModel, Field, condecimal, conint, constr, EmailStr
from typing import Optional, List

class Base(BaseModel):
    class Config:
        from_attributes = True  # Для совместимости с ORM (ранее `orm_mode = True`)

# Модель для таблицы "restaurants"
class RestaurantBase(Base):
    name: constr(max_length=100)
    description: Optional[str] = None
    address: constr(max_length=255)
    phone_number: constr(max_length=20)
    rating: Optional[condecimal(max_digits=3, decimal_places=2)] = Field(default=0, ge=0, le=5)
    created_at: Optional[datetime] = None

class RestaurantCreate(RestaurantBase):
    pass

class Restaurant(RestaurantBase):
    restaurant_id: int

# Модель для таблицы "users"
class UserBase(Base):
    username: constr(max_length=50)
    email: EmailStr
    is_vip: Optional[bool] = False
    created_at: Optional[datetime] = None

class UserCreate(UserBase):
    password_hash: constr(max_length=255)

class User(UserBase):
    user_id: int

# Модель для таблицы "reviews"
class ReviewBase(Base):
    restaurant_id: int
    user_id: int
    rating: conint(ge=1, le=5)
    comment: Optional[str] = None
    created_at: Optional[datetime] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    review_id: int

# Модель для таблицы "reservations"
class ReservationBase(Base):
    user_id: int
    restaurant_id: int
    reservation_date: datetime
    guests_number: conint(gt=0)
    status: constr(max_length=20) = Field(default="pending")
    created_at: Optional[datetime] = None

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    reservation_id: int

# Модель для таблицы "orders"
class OrderBase(Base):
    user_id: int
    restaurant_id: int
    order_date: Optional[datetime] = None
    total_amount: condecimal(max_digits=10, decimal_places=2, ge=0)
    status: constr(max_length=20) = Field(default="pending")

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int

# Модель для таблицы "order_items"
class OrderItemBase(Base):
    order_id: int
    item_name: constr(max_length=100)
    quantity: conint(gt=0)
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    total_price: condecimal(max_digits=10, decimal_places=2, ge=0)

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: int

# Модель для таблицы "bonuses"
class BonusBase(Base):
    user_id: int
    points: conint(ge=0) = Field(default=0)
    description: Optional[constr(max_length=255)] = None
    expiration_date: Optional[datetime] = None
    created_at: Optional[datetime] = None

class BonusCreate(BonusBase):
    pass

class Bonus(BonusBase):
    bonus_id: int

# Модель для таблицы "restaurant_bonuses"
class RestaurantBonusBase(Base):
    restaurant_id: int
    description: constr(max_length=255)
    points_required: conint(gt=0)
    discount_percentage: condecimal(max_digits=5, decimal_places=2, ge=0, le=100)
    created_at: Optional[datetime] = None

class RestaurantBonusCreate(RestaurantBonusBase):
    pass

class RestaurantBonus(RestaurantBonusBase):
    restaurant_bonus_id: int

# Модель для таблицы "user_bonus_redeem"
class UserBonusRedeemBase(Base):
    user_id: int
    restaurant_bonus_id: int
    redeemed_at: Optional[datetime] = None

class UserBonusRedeemCreate(UserBonusRedeemBase):
    pass

class UserBonusRedeem(UserBonusRedeemBase):
    redeem_id: int