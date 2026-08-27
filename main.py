from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>Farol da Alma - Online</h1><p>Em manutencao</p>"

@app.get("/health")
def health():
    return {"status": "ok"}
