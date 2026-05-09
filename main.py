from fastapi import FastAPI
from infrastructure.db import engine, Base
from api import usuarios, auth, pedidos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Raízes do Nordeste",
    description="API para gestão da rede de lanchonetes.",
    version="1.0.0"
)

# Rotas
app.include_router(usuarios.router)
app.include_router(auth.router)
app.include_router(pedidos.router)

@app.get("/")
def raiz():
    return {"mensagem": "API Raízes do Nordeste iniciada!"}