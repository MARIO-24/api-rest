from db import get_connection
from schemas import ClienteCreate, ClienteUpdate

# ========================
# CRUD DE CLIENTES
# ========================

def get_clientes():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes")
            result = cursor.fetchall()
        return result
    finally:
        conn.close()

def get_cliente(id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes WHERE id=%s", (id,))
            result = cursor.fetchone()
        return result
    finally:
        conn.close()

def create_cliente(cliente: ClienteCreate):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO clientes
                     (nombre, apellido, email, telefono, fecha_nacimiento, genero, tipo_membresia, activo)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                cliente.nombre,
                cliente.apellido,
                cliente.email,
                cliente.telefono,
                cliente.fecha_nacimiento,
                cliente.genero,
                cliente.tipo_membresia,
                cliente.activo
            ))
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()

def update_cliente(id: int, cliente: ClienteUpdate):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            campos = []
            valores = []
            for key, value in cliente.dict(exclude_unset=True).items():
                campos.append(f"{key}=%s")
                valores.append(value)
            
            if not campos:
                return  # No hay campos para actualizar
            
            valores.append(id)
            sql = f"UPDATE clientes SET {', '.join(campos)} WHERE id=%s"
            cursor.execute(sql, valores)
        conn.commit()
    finally:
        conn.close()

def delete_cliente(id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        conn.commit()
    finally:
        conn.close()
