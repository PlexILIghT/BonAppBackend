from bonAppBackend.database import engine, Base
from bonAppBackend.models import (
    Restaurant,
    User,
    Review,
    Reservation,
    Order,
    OrderItem,
    Bonus,
    RestaurantBonus,
    UserBonusRedeem,
)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
