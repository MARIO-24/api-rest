from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None
    tipo_membresia: Optional[str] = None
    activo: Optional[int] = 1

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None
    tipo_membresia: Optional[str] = None
    activo: Optional[int] = None

class ClienteOut(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None
    tipo_membresia: Optional[str] = None
    fecha_alta: Optional[str] = None
    activo: Optional[int] = None
