from fastapi import FastAPI , HTTPException

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        del items[item_id]