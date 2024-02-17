from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role


app = FastAPI()

db: List[User] = [
    User(id =UUID("50521ca7-c160-4960-a6c9-7e787e834b3f"),
        first_name="Camila",
        last_name="Santos",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(id =UUID("6e51dbd9-5147-491a-aaec-6736d0e045f5"),
        first_name="Quesia",
        last_name="Moraes",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(id =UUID("d4d9112b-836e-4a5e-bc43-4428572c7fe7"),
        first_name="Cintia",
        last_name="Silva",
        email="email@gmail.com",
        role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"}

@app.post("/api/users")
async def add_user(user:User):
    """
    Adicionar um usuário na base de dados
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: List[Role]
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail= f"Usuário com id {id} não encontrado"
    )
