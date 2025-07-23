from fastapi import FastAPI, HTTPException
from models import User
from database import collection
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    user_dict = jsonable_encoder(user)
    result = collection.insert_one(user_dict)
    return {"id": str(result.inserted_id)}

@app.get("/users")
def get_users():
    users = list(collection.find())
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    return users

@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user["_id"])
    del user["_id"]
    return user
