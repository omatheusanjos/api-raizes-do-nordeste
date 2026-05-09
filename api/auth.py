import jwt
import hashlib
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from infrastructure.db import get_db
from domain.models import Usuario

router = APIRouter()

SECRET_KEY = "chave_secreta_super_segura_do_projeto"
ALGORITHM = "HS256"

# Schema para o Request de Login
class LoginRequest(BaseModel):
    email: str
    senha: str

@router.post("/auth/login", status_code=200, tags=["Autenticação"])
def login(requisicao: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == requisicao.email).first()
    
    senha_criptografada = hashlib.sha256(requisicao.senha.encode()).hexdigest()

    if not usuario or usuario.senha_hash != senha_criptografada:
        raise HTTPException(status_code=401, detail="CREDENCIAIS_INVALIDAS: E-mail ou senha inválidos.")
    
    # Gerar o Token JWT com validade de 1 hora
    dados_token = {
        "sub": usuario.id,
        "perfil": usuario.perfil,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(dados_token, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "accessToken": token,
        "tokenType": "Bearer",
        "expiresIn": 3600,
        "user": {
            "id": usuario.id,
            "nome": usuario.nome,
            "perfil": usuario.perfil
        }
    }