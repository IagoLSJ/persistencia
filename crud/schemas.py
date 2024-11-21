from pydantic import BaseModel
from typing import Optional

class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano: int
    genero: str

class LivroCreate(LivroBase):
    id: int

class LivroResponse(LivroBase):
    id: int
