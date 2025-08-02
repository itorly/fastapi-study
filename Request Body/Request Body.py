from fastapi import FastAPI
from pydantic import BaseModel

# Create some data model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

# Declare it as a parameter
@app.post("/items/")
async def create_item(item: Item):
    return item