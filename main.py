from fastapi import FastAPI
from dishes import routers as dish_rout
from orders import routers as order_rout

app = FastAPI()

app.include_router(dish_rout.router)
app.include_router(order_rout.router)
