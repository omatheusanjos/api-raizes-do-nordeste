import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, Integer, ForeignKey, DateTime
from infrastructure.db import Base

def generate_uuid():
    return str(uuid.uuid4())

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(String, primary_key=True, default=generate_uuid)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False) # LGPD
    perfil = Column(String, default="CLIENTE")
    consentimento_lgpd = Column(Boolean, default=True)

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(String, primary_key=True, default=generate_uuid)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(String, primary_key=True, default=generate_uuid)
    cliente_id = Column(String, ForeignKey("usuarios.id"))
    unidade_id = Column(String, nullable=False)
    canal_pedido = Column(String, nullable=False)
    status = Column(String, default="AGUARDANDO_PAGAMENTO")
    valor_total = Column(Float, default=0.0)
    data_criacao = Column(DateTime, default=datetime.utcnow)

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id = Column(String, primary_key=True, default=generate_uuid)
    pedido_id = Column(String, ForeignKey("pedidos.id"))
    produto_id = Column(String, ForeignKey("produtos.id"))
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

class Pagamento(Base):
    __tablename__ = "pagamentos"
    id = Column(String, primary_key=True, default=generate_uuid)
    pedido_id = Column(String, ForeignKey("pedidos.id"))
    status_gateway = Column(String, nullable=False)
    data_pagamento = Column(DateTime, default=datetime.utcnow)