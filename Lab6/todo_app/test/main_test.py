from fastapi.testclient import TestClient
from Lab6.todo_app.src.main import app  
client = TestClient(app)


def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}


def test_first_apiV2():
    response = client.get("/books/test_path_param")
    assert response.status_code == 200
    assert response.json() == {"msg": "test_path_param"}


def test_first_apiV3():
    response = client.get("/books/", params={"title": "test_title"})
    assert response.status_code == 200
    assert response.json() == {"msg": "test_title"}


def test_first_apiV4():
    response = client.get("/books/create_book", json={"new_book": "test_book"})
    assert response.status_code == 200
    assert response.json() == {"msg": {"new_book": "test_book"}}


def test_create_item():
    test_item = {"key": "value"}
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    assert response.json() == {"item": test_item}


def test_update_item():
    test_item = {"key": "new_value"}
    response = client.put("/items/1", json=test_item)
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "updated_item": test_item}


def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted."}
