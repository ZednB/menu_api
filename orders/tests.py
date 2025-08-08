from datetime import datetime

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

EXISTING_DISH_IDS = [1, 2]
NONE_EXISTING_DISH_IDS = [100]


def test_create_order_success():
    response = client.post("/orders/", json=
    {
        "customer_name": "Иван",
        "order_time": datetime.utcnow().isoformat(),
        "status": "В обработке",
        "dishes": EXISTING_DISH_IDS
    }
                           )
    assert response.status_code == 201
    data = response.json()
    assert data['customer_name'] == "Иван"
    assert data['status'] == "В обработке"
    assert len(data['dishes']) == len(EXISTING_DISH_IDS)


def test_create_order_with_invalid_dish():
    response = client.post("/orders/", json=
    {
        "customer_name": "Иван",
        "order_time": datetime.utcnow().isoformat(),
        "status": "В обработке",
        "dishes": NONE_EXISTING_DISH_IDS
    }
                           )
    ids_str = ", ".join(map(str, NONE_EXISTING_DISH_IDS))
    assert response.status_code == 400
    assert f"Блюдо с id {ids_str} не найдено" in response.json()['detail']


def test_valid_status_transition():
    create_response = client.post('/orders/', json={
        "customer_name": "Иван",
        "order_time": datetime.utcnow().isoformat(),
        "status": "В обработке",
        "dishes": EXISTING_DISH_IDS
    })
    order_id = create_response.json()['id']
    update_response = client.put(f"/orders/{order_id}", json={"status": "Готовится"})
    assert update_response.status_code == 200
    assert update_response.json()['status'] == 'Готовится'


def test_invalid_status_transition():
    create_response = client.post('/orders/', json={
        "customer_name": "Иван",
        "order_time": datetime.utcnow().isoformat(),
        "status": "В обработке",
        "dishes": EXISTING_DISH_IDS
    })
    order_id = create_response.json()['id']
    update_response = client.put(f"/orders/{order_id}", json={"status": "Доставляется"})
    assert update_response.status_code == 400
    assert f"Неправильное изменение статуса: " in update_response.json()['detail']


def test_delete_order():
    create_response = client.post('/orders/', json={
        "customer_name": "Иван",
        "order_time": datetime.utcnow().isoformat(),
        "status": "В обработке",
        "dishes": EXISTING_DISH_IDS
    })
    order_id = create_response.json()['id']
    cancel_resp = client.delete(f"/orders/{order_id}")
    assert cancel_resp.status_code == 200
