from datetime import date, datetime
from typing import Optional

class Cliente:
    id: int
    nombre: str
    apellido: str
    email: Optional[str]
    telefono: Optional[str]
    fecha_nacimiento: Optional[date]
    genero: Optional[str]
    tipo_membresia: Optional[str]
    fecha_alta: Optional[datetime]
    activo: Optional[int]
