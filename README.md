# Menu API

Приложение для управления заказами и блюдами, упакованное в Docker.

## Установка и запуск

### Вариант 1 — Запуск в Docker (рекомендуется)

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/menu-api.git
   cd menu-api
Запустите контейнеры:
docker-compose up --build

Приложение будет доступно по адресу:
http://localhost:8000


Вариант 2 — Локальный запуск без Docker
Клонируйте репозиторий:
git clone https://github.com/yourusername/menu-api.git
cd menu-api

Создайте виртуальное окружение и активируйте его:
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Установите зависимости:
pip install -r requirements.txt

Настройте переменные окружения.
Создайте .env файл или задайте переменные окружения вручную:
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/menu_db

Запустите миграции Alembic (если используются):
alembic upgrade head

Запустите приложение:
uvicorn main:app --reload

API Endpoints
POST /orders/ — Создать заказ
GET /orders/{order_id} — Получить заказ по ID
PATCH /orders/{order_id} — Обновить заказ (например, статус)
DELETE /orders/{order_id} — Отменить заказ
POST /dishes/ — Создать блюдо
GET /dishes/{dish_id} — Получить блюдо по ID
(и другие...)

Тестирование
Запустите тесты с помощью pytest:
pytest