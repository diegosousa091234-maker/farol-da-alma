from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, json
from datetime import datetime

app = FastAPI()
MEM_FILE = "memoria.json"
CHAVE_MESTRE = "farol2026"
CHAVE_ALUNO = "aluno123"

def load():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE,"r",encoding="utf-8") as f:
                return json.load(f)
        except: return {}
    return {}

def save(d):
    with open(MEM_FILE,"w",encoding="utf-8") as f:
        json.dump(d,f,ensure_ascii=False,indent=2)

@app.get("/api/login/{chave}/{nome}")
def login(chave: str, nome: str):
    mem = load()
    if chave == CHAVE_MESTRE:
        tipo = "mestre"
    elif chave == CHAVE_ALUNO:
        tipo = "aluno"
    else:
        return {"ok": False, "erro": "Chave incorreta! Use farol2026 (mestre) ou aluno123 (aluno)"}
    
    mem["usuario_atual"] = {"nome": nome, "tipo": tipo, "logado": True}
    mem["nome"] = nome
    hist = mem.get("historico", [])
    hist.append({"evento": f"Login {tipo}: {nome}", "hora": datetime.now().strftime("%H:%M")})
    mem["historico"] = hist[-50:]
    save(mem)
    return {"ok": True, "nome": nome, "tipo": tipo}

@app.get("/api/oraculo/{pergunta}")
def oraculo(pergunta: str):
    mem = load()
    user = mem.get("usuario_atual", {})
    if not user.get("logado"):
        return {"resposta": "🛡️ DIGITE A CHAVE primeiro para entrar POR DENTRO."}
    nome = user.get("nome","Guerreiro")
    tipo = user.get("tipo","aluno")
    p = pergunta.lower()
    
    hist = mem.get("historico", [])
    hist.append({"pergunta": pergunta, "por": nome})
    mem["historico"] = hist[-50:]
    save(mem)

    tag = f"[{tipo.upper()} {nome}]"
    if "tempra" in p or "forja" in p:
        if tipo == "mestre":
            return {"resposta": f"🔥 {tag} TEMPRA FORJA MESTRE liberada! Você tem poder total sobre o Farol, {nome}. Forjando a estrutura!"}
        else:
            return {"resposta": f"🔥 {tag} TEMPRA FORJA ALUNO: {nome}, sua alma está sendo forjada. O Mestre está vendo seu progresso."}
    if "seguranca" in p:
        return {"resposta": f"🛡️ {tag} SEGURANÇA: Logado como {tipo}. {len(hist)} registros. Imagem oficial ativa."}
    return {"resposta": f"🔥 {tag} POR DENTRO: '{pergunta}' recebido. Você está conversando dentro do Farol com a imagem oficial ativa."}

@app.get("/")
def home(): return FileResponse("index.html")
