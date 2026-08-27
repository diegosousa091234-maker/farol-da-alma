
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, json
from datetime import datetime

app = FastAPI()
MEM_FILE = "memoria.json"

# PEGA A SENHA DO RENDER, NÃO DO CÓDIGO
CHAVE_MESTRA = os.getenv("FAROL_KEY", "farol2026") 

def load():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return {}
    return {}

def save(d):
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

@app.get("/api/login/{chave}/{tipo}/{nome}")
def login(chave: str, tipo: str, nome: str):
    if chave != CHAVE_MESTRA:
        return {"ok": False, "erro": "Chave incorreta!"}
    mem = load()
    mem["usuario_atual"] = {"nome": nome, "tipo": tipo, "logado": True}
    mem["nome"] = nome
    mem["historico"] = mem.get("historico", [])[-50:]
    save(mem)
    return {"ok": True, "nome": nome, "tipo": tipo}

@app.get("/api/oraculo/{pergunta}")
def oraculo(pergunta: str):
    mem = load()
    user = mem.get("usuario_atual", {})
    if not user.get("logado"):
        return {"resposta": "🛡️ Faça login."}
    return {"resposta": f"🔥 [{user.get('tipo').upper()} {user.get('nome')}] POR DENTRO: '{pergunta}' - sistema seguro com chave oculta."}

@app.get("/")
def home():
    return FileResponse("index.html")
