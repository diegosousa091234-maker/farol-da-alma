from datetime import datetime, timedelta
import jwt
from config import Config
def criar_token(usuario: str):
    expira = datetime.utcnow() + timedelta(minutes=Config.TEMPO_TOKEN)
    payload = {"usuario": usuario, "exp": expira}
    return jwt.encode(payload, Config.CHAVE_SECRETA, algorithm=Config.ALGORITMO)
def verificar_token(token: str):
    try:
        dados = jwt.decode(token, Config.CHAVE_SECRETA, algorithms=[Config.ALGORITMO])
        return dados["usuario"]
    except:
        return None
