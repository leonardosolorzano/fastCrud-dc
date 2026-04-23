from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=150)
    email: EmailStr = Field(max_length=200)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=False)
    
    id: str
    image_file: str | None
    image_path: str


# Publicacion de posts esqueleto para que pueda documentar el codigo
# dentro de la api, o de la interfaz de fastapi
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=500)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    # model_config nos permite configurar el comportamiento de
    # Pydantic para que pueda trabajar con objetos ORM
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
