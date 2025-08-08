# Menu API

API для управления заказами и блюдами кафе/ресторана.

## Описание проекта

Этот проект реализует backend на FastAPI для работы с заказами и блюдами.  
Позволяет создавать, обновлять, удалять и просматривать заказы и блюда.  
Используется PostgreSQL как база данных с SQLAlchemy ORM.

---

## Стек технологий

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic (v2)
- Alembic (миграции)
- pytest (тесты)

---

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/yourusername/menu-api.git
cd menu-api

2. Создайте виртуальное окружение и активируйте его
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Установите зависимости
pip install -r requirements.txt

4. Настройте переменные окружения
Создайте .env файл или настройте переменные окружения с параметрами подключения к базе данных, например:
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/menu_db

5. Запустите миграции Alembic (если используются)
alembic upgrade head

6. Запустите приложение
uvicorn main:app --reload

API Endpoints
POST /orders/ — Создать заказ

GET /orders/{order_id} — Получить заказ по ID

PATCH /orders/{order_id} — Обновить заказ (например, статус)

DELETE /orders/{order_id} — Отменить заказ

POST /dishes/ — Создать блюдо

GET /dishes/{dish_id} — Получить блюдо по ID

и другие...

Тестирование
Запустите тесты с помощью pytest:
pytest


