from pydantic import BaseModel
from typing import List

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    consentimentoLgpd: bool

class ItemPedidoCreate(BaseModel):
    produtoId: str
    quantidade: int

class PedidoCreate(BaseModel):
    canalPedido: str
    unidadeId: str
    itens: List[ItemPedidoCreate]
    formaPagamento: str