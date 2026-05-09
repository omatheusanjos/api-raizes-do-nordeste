from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from infrastructure.db import get_db
from domain.models import Pedido, ItemPedido, Pagamento
from domain.schemas import PedidoCreate

router = APIRouter()

class PagamentoMockRequest(BaseModel):
    pedidoId: str
    valor: float
    metodo: str

class AtualizarStatusRequest(BaseModel):
    status: str

# CRIAR PEDIDO
@router.post("/pedidos", status_code=201, tags=["Pedidos"])
def criar_pedido(pedido_req: PedidoCreate, db: Session = Depends(get_db)):
    canais_aceitos = ["APP", "TOTEM", "BALCAO", "PICKUP", "WEB"]
    if pedido_req.canalPedido.upper() not in canais_aceitos:
        raise HTTPException(status_code=400, detail="CANAL_INVALIDO: O canalPedido informado é inválido.")

    valor_total = 0.0
    for item in pedido_req.itens:
        if item.quantidade > 50: # Restrição de Estoque simulada
            raise HTTPException(status_code=409, detail="ESTOQUE_INSUFICIENTE: Quantidade indisponível na unidade.")
        valor_total += item.quantidade * 35.90 

    novo_pedido = Pedido(
        unidade_id=pedido_req.unidadeId,
        canal_pedido=pedido_req.canalPedido.upper(),
        valor_total=valor_total
    )
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    for item in pedido_req.itens:
        novo_item = ItemPedido(
            pedido_id=novo_pedido.id, produto_id=item.produtoId, 
            quantidade=item.quantidade, preco_unitario=35.90
        )
        db.add(novo_item)
    db.commit()

    return {
        "pedidoId": novo_pedido.id,
        "status": novo_pedido.status,
        "total": novo_pedido.valor_total,
        "canalPedido": novo_pedido.canal_pedido
    }

# PAGAMENTO
@router.post("/pagamentos/mock", status_code=200, tags=["Pagamentos"])
def processar_pagamento_mock(req: PagamentoMockRequest, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == req.pedidoId).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="PEDIDO_NAO_ENCONTRADO: O pedido informado não existe.")

    novo_pagamento = Pagamento(pedido_id=pedido.id, status_gateway="APROVADO")
    db.add(novo_pagamento)
    
    pedido.status = "PAGO"
    db.commit()

    return {
        "transacaoId": novo_pagamento.id,
        "pedidoId": pedido.id,
        "statusGateway": "APROVADO",
        "mensagem": "Pagamento simulado aprovado e pedido atualizado."
    }

# ATUALIZAR STATUS
@router.patch("/pedidos/{pedido_id}/status", status_code=200, tags=["Pedidos"])
def atualizar_status(pedido_id: str, req: AtualizarStatusRequest, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    status_anterior = pedido.status
    pedido.status = req.status.upper() 
    db.commit()

    return {
        "pedidoId": pedido.id,
        "statusAnterior": status_anterior,
        "statusAtual": pedido.status
    }