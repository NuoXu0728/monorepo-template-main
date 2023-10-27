from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api")
def first_api():
    return {"msg": "hello_world"}


@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}


@app.get("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted."}