from fastapi import APIRouter 
from pydantic import BaseModel
from datetime import datetime
user = APIRouter()
users = []

#@userModel
class model_user(BaseModel):
    id:str
    usuario:str
    contraseña:str
    create_at:datetime=datetime.now()
    estatus:bool=False


@user.get("/")



def bienvenida():
    return "Hola 9b"


@user.get("/user")

def usaurio():
    return users


#metodo post 
@user.post("/users")

def save_users(insert_users:model_user):
    users.append(insert_users)
    print(insert_users)
    return "Datos guardados"
