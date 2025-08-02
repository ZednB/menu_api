from fastapi import FastAPI
from dishes import routers

app = FastAPI()

app.include_router(routers.router)
