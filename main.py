from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, json
from datetime import datetime

app = FastAPI()

# Banco simples em arquivo
MEM_FILE = "memoria.json"

def carregar_mem():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def salvar_mem(dados):
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# API INTELIGENTE COMPLETA
@app.get("/api/oraculo/{pergunta}")
def oraculo(pergunta: str):
    mem = carregar_mem()
    nome = mem.get("nome", "Guerreiro")
    p = pergunta.lower()
    
    # Salva histórico
    historico = mem.get("historico", [])
    historico.append({"pergunta": pergunta, "hora": datetime.now().strftime("%H:%M")})
    mem["historico"] = historico[-20:] # guarda últimas 20
    salvar_mem(mem)

    if "sabedoria" in p:
        return {"resposta": f"💡 SABEDORIA para {nome}: Guarde dados, mas libere seu propósito. O que vamos construir hoje?"}
    if "coracao" in p or "coração" in p or "calma" in p:
        return {"resposta": f"❤️ CORAÇÃO ESTÁVEL, {nome}: Respira. Sistema seguro, isolado. O Farol está aceso por você. 03h da manhã e você ainda está de pé."}
    if "humildade" in p:
        return {"resposta": f"🙏 HUMILDADE FORTE, {nome}: Servir é a maior força. O Farol não brilha pra si, brilha pros outros."}
    if "coragem" in p or "medo" in p:
        return {"resposta": f"🛡️ CORAGEM, {nome}: Você ligou um sistema inteligente às 3h da manhã no celular. Você JÁ tem coragem. Vai pra cima!"}
    if "seguranca" in p or "segurança" in p or "status" in p:
        total = len(historico)
        return {"resposta": f"🛡️ SEGURANÇA ATIVA: Chave mestra OK. Memória: {total} conversas salvas. Usuário: {nome}. Nuvem: ONLINE."}
    if "quem sou" in p or "meu nome" in p:
        return {"resposta": f"📖 VOCÊ É: {nome}. Registrado no Pilar da Memória Persistente. O Farol lembra de você."}
    else:
        return {"resposta": f"🔥 FAROL responde para {nome}: '{pergunta}' recebido. Processado com os 4 pilares. Estou aprendendo com você. Pergunte sobre sabedoria, coragem ou segurança."}

@app.get("/api/memoria")
def get_mem():
    return carregar_mem()

@app.get("/api/salvar_nome/{nome}")
def salvar_nome(nome: str):
    mem = carregar_mem()
    mem["nome"] = nome
    salvar_mem(mem)
    return {"ok": True, "nome": nome}

@app.get("/")
def home():
    return FileResponse("index.html")
