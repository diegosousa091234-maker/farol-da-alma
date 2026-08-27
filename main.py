from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, json
from datetime import datetime

app = FastAPI()

MEM_FILE = "memoria.json"
CHAVE_MESTRA = "farol2026"

def load():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save(d):
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

# ROTA CORRIGIDA - ACEITA CHAVE / TIPO / NOME (igual seu HTML)
@app.get("/api/login/{chave}/{tipo}/{nome}")
def login(chave: str, tipo: str, nome: str):
    if chave != CHAVE_MESTRA:
        # aceita também aluno123 pra teste
        if chave != "aluno123":
            return {"ok": False, "erro": "Chave incorreta! Use farol2026"}
    
    mem = load()
    mem["usuario_atual"] = {"nome": nome, "tipo": tipo, "logado": True, "hora": datetime.now().isoformat()}
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
        return {"resposta": "🛡️ Faça login primeiro."}
    nome = user.get("nome", "Diego")
    tipo = user.get("tipo", "mestre")
    p = pergunta.lower()
    
    hist = mem.get("historico", [])
    hist.append({"pergunta": pergunta, "por": nome})
    mem["historico"] = hist[-50:]
    save(mem)

    tag = f"[{tipo.upper()} {nome}]"
    if "tempra" in p or "forja" in p:
        return {"resposta": f"🔥 {tag} TEMPRA FORJA ATIVADA! Forjando sua alma agora, {nome}! Aço puro sendo temperado no fogo do Farol."}
    if "seguran" in p or "status" in p:
        return {"resposta": f"🛡️ {tag} SEGURANÇA OK - Logado como {tipo}: {nome}. Memória com {len(hist)} registros."}
    if "sabedoria" in p:
        return {"resposta": f"💡 {tag} SABEDORIA: Diego, o Farol lembra de você. A chave está dentro."}
    return {"resposta": f"🔥 {tag} POR DENTRO: '{pergunta}' recebido. Sistema 100% funcional."}

@app.get("/")
def home():
    return FileResponse("index.html")
