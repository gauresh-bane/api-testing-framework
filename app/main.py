from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="User Management API", version="1.0.0")

# In-memory database
users_db = {}
user_id_counter = 1

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: int
    created_at: Optional[str] = None

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to User Management API"}

@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    global user_id_counter
    
    # Check if email already exists
    for existing_id, existing_user in users_db.items():
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    return new_user

@app.get("/users/", response_model=List[User])
def get_users():
    return list(users_db.values())

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = users_db[user_id]
    if user_update.name is not None:
        user["name"] = user_update.name
    if user_update.email is not None:
        # Check if new email already exists
        for existing_id, existing_user in users_db.items():
            if existing_id != user_id and existing_user["email"] == user_update.email:
                raise HTTPException(status_code=400, detail="Email already registered")
        user["email"] = user_update.email
    if user_update.age is not None:
        user["age"] = user_update.age
    
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)