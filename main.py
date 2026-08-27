from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from pathlib import Path

app = FastAPI()

# Cria pastas se não existirem pra não quebrar o deploy
for pasta in ["css", "js", "imagens", "paginas"]:
    Path(pasta).mkdir(exist_ok=True)

# Monta os estáticos só se existirem
if Path("css").exists():
    app.mount("/css", StaticFiles(directory="css"), name="css")
if Path("js").exists():
    app.mount("/js", StaticFiles(directory="js"), name="js")
if Path("imagens").exists():
    app.mount("/imagens", StaticFiles(directory="imagens"), name="imagens")
if Path("paginas").exists():
    app.mount("/paginas", StaticFiles(directory="paginas"), name="paginas")

@app.get("/")
def home():
    if Path("index.html").exists():
        return FileResponse("index.html")
    return {"status": "Farol da Alma - estrutura subindo", "service": "srv-da7s8ioae00c739vlfng"}

@app.get("/health")
def health():
    return {"status": "live", "frequencia": "firme"}

# Serve qualquer pagina.html direto
@app.get("/{pag}")
def serve_pag(pag: str):
    if Path(pag).exists() and Path(pag).is_file():
        return FileResponse(pag)
    if Path(f"paginas/{pag}").exists():
        return FileResponse(f"paginas/{pag}")
    if Path("index.html").exists():
        return FileResponse("index.html")
    return {"erro": "pagina nao encontrada"}
