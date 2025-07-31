from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from core.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root(db: Session = Depends(get_db)):
    return {'message': 'База данных подключена'}
