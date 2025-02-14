from bonAppBackend.database import SessionLocal
from bonAppBackend.models import Restaurant, User

def seed_db():
    db = SessionLocal()

    # Добавление ресторанов
    restaurants = [
        Restaurant(name="Ресторан 1", address="Адрес 1", phone_number="+1234567890"),
        Restaurant(name="Ресторан 2", address="Адрес 2", phone_number="+0987654321"),
    ]
    db.add_all(restaurants)

    # Добавление пользователей
    users = [
        User(username="user1", email="user1@example.com", password_hash="hash1"),
        User(username="user2", email="user2@example.com", password_hash="hash2"),
    ]
    db.add_all(users)

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_db()