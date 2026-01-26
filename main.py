from fastapi import FastAPI, HTTPException
from typing import List
from crud import get_clientes, get_cliente, create_cliente, update_cliente, delete_cliente
from schemas import ClienteCreate, ClienteUpdate, ClienteOut

app = FastAPI(title="API REST Gym")

@app.get("/clientes", response_model=List[ClienteOut])
def listar_clientes():
    return get_clientes()

@app.get("/clientes/{id}", response_model=ClienteOut)
def obtener_cliente(id: int):
    cliente = get_cliente(id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/clientes", response_model=int)
def agregar_cliente(cliente: ClienteCreate):
    id_nuevo = create_cliente(cliente)
    return id_nuevo

@app.put("/clientes/{id}", response_model=dict)
def modificar_cliente(id: int, cliente: ClienteUpdate):
    existente = get_cliente(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    update_cliente(id, cliente)
    return {"mensaje": "Cliente actualizado"}


@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    if not get_cliente(id):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    delete_cliente(id)
    return {"mensaje": "Cliente eliminado"}
