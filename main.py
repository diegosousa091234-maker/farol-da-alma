
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Rota da Inteligência do Farol
@app.get("/api/oraculo/{pergunta}")
def oraculo(pergunta: str):
    pergunta = pergunta.lower()
    if "sabedoria" in pergunta:
        return {"resposta": "💡 SABEDORIA: A sabedoria do Farol diz: Guarde seus dados, mas libere seu propósito. O que você quer construir hoje?"}
    if "coracao" in pergunta or "coração" in pergunta:
        return {"resposta": "❤️ CORAÇÃO ESTÁVEL: Mantenha a calma. O sistema está seguro e isolado. Respire. O Farol está aceso por você."}
    if "humildade" in pergunta:
        return {"resposta": "🙏 HUMILDADE FORTE: Servir é a maior força. O Farol não brilha pra si, brilha pros outros."}
    if "coragem" in pergunta:
        return {"resposta": "🛡️ CORAGEM: Você já acendeu um site às 03h da manhã no celular. Você já tem coragem."}
    if "seguranca" in pergunta or "segurança" in pergunta:
        return {"resposta": "🛡️ SEGURANÇA: Chave mestra ativa. Acesso controlado. Seus dados estão em cofre imutável."}
    else:
        return {"resposta": f"🔥 FAROL DA ALMA responde: Recebi sua pergunta '{pergunta}'. Estou processando com Sabedoria, Coração Estável, Humildade e Coragem. Sistema ONLINE."}

@app.get("/")
def home():
    return FileResponse("index.html")

app.mount("/static", StaticFiles(directory="."), name="static")
