from fastapi import FastAPI
from .endpoints import (
    restaurants,
    users,
    reviews,
    reservations,
    orders,
    bonuses,
    restaurant_bonuses,
)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(restaurants.router)
app.include_router(users.router)
app.include_router(reviews.router)
app.include_router(reservations.router)
app.include_router(orders.router)
app.include_router(bonuses.router)
app.include_router(restaurant_bonuses.router)