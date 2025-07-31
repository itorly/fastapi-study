from fastapi import FastAPI

app = FastAPI()

# path "parameters" or "variables"
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types
@app.get("/ints/{int_id}")
async def read_int(int_id: int):
    return {"int_id": int_id}