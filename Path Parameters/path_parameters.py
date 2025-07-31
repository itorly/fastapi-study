from fastapi import FastAPI

app = FastAPI()

# path "parameters" or "variables"
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

