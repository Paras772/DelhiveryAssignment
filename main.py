from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

# Initialize FastAPI app
app = FastAPI()

# Define a Pydantic model for the request/response schema
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI App!"}

# Get an item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    logger.info(f"Read item endpoint accessed with item_id={item_id}, q={q}")
    return {"item_id": item_id, "q": q}

# Create an item
@app.post("/items/")
def create_item(item: Item):
    logger.info(f"Create item endpoint accessed with item={item}")
    total_price = item.price + (item.tax or 0)
    logger.info(f"Calculated total_price={total_price}")
    return {"item": item, "total_price": total_price}

# Health check endpoint
@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}

# To run the app locally:
# uvicorn main:app --reload