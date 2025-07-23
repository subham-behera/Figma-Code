from fastapi import FastAPI, HTTPException
from models import Product
from database import collection
from bson import ObjectId

app = FastAPI()

@app.get("/products")
def get_products():
    products = list(collection.find({}, {"_id": 0}))
    return products

@app.post("/products")
def add_product(product: Product):
    collection.insert_one(product.dict())
    return {"message": "Product added"}

@app.delete("/products/{name}")
def delete_product(name: str):
    result = collection.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
