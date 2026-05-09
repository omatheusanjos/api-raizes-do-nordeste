import hashlib
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.db import get_db
from domain.models import Usuario
from domain.schemas import UsuarioCreate

router = APIRouter()

@router.post("/usuarios", status_code=201, tags=["Usuários"])
def cadastrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar a LGPD
    if not usuario.consentimentoLgpd:
        raise HTTPException(status_code=400, detail="O aceite dos termos da LGPD é obrigatório.")

    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=409, detail="E-mail já cadastrado.")
    
    senha_criptografada = hashlib.sha256(usuario.senha.encode()).hexdigest()
    
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=senha_criptografada,
        consentimento_lgpd=usuario.consentimentoLgpd
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email,
        "perfil": novo_usuario.perfil,
        "consentimento_lgpd": novo_usuario.consentimento_lgpd
    }