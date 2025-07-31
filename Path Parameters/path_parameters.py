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

# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]