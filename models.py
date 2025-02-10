from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Restaurant(Base):
    __tablename__ = "restaurants"
    restaurant_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(Text)
    address = Column(String(255))
    phone_number = Column(String(20))
    rating = Column(Numeric(3, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_vip = Column(Boolean, default=False)

class Review(Base):
    __tablename__ = "reviews"
    review_id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Reservation(Base):
    __tablename__ = "reservations"
    reservation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    reservation_date = Column(DateTime, nullable=False)
    guests_number = Column(Integer)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), default="pending")

class OrderItem(Base):
    __tablename__ = "order_items"
    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    item_name = Column(String(100), nullable=False)
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    total_price = Column(Numeric(10, 2))

class Bonus(Base):
    __tablename__ = "bonuses"
    bonus_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    points = Column(Integer, default=0)
    description = Column(String(255))
    expiration_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

class RestaurantBonus(Base):
    __tablename__ = "restaurant_bonuses"
    restaurant_bonus_id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    description = Column(String(255))
    points_required = Column(Integer)
    discount_percentage = Column(Numeric(5, 2))
    created_at = Column(DateTime, default=datetime.utcnow)

class UserBonusRedeem(Base):
    __tablename__ = "user_bonus_redeem"
    redeem_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    restaurant_bonus_id = Column(Integer, ForeignKey("restaurant_bonuses.restaurant_bonus_id"))
    redeemed_at = Column(DateTime, default=datetime.utcnow)
