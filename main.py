import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
CHAVE = os.getenv("FAROL_KEY", "BrasaSabedoriaforja").strip()

HTML = """
<body style='background:#000;color:#c9a86a;display:flex;justify-content:center;align-items:center;min-height:100vh'><div style='border:1px solid #c9a86a;padding:30px;border-radius:20px;text-align:center'>
<h2>TEMPORA - FAROL DA ALMA</h2>
<form method=POST>
<input name=nome placeholder='Nome' required style='padding:12px;width:90%'><br><br>
<input id=s name=chave type=password placeholder='Chave' required style='padding:12px;width:70%'>
<span onclick="s.type=s.type=='password'?'text':'password'"> 👁️</span><br><br>
<button style='padding:15px;width:100%;background:#c9a86a;border:none'>ACENDER MEU FAROL</button>
</form><p style=color:red>{erro}</p>
</div></body>
"""

@app.get("/", response_class=HTMLResponse)
def get(): return HTML.format(erro="")

@app.post("/", response_class=HTMLResponse)
def post(nome: str = Form(...), chave: str = Form(...)):
    if chave.strip() == CHAVE:
        return f"<h1 style='background:#000;color:#c9a86a;text-align:center;padding:100px'>BEM-VINDO {nome}! FAROL ACESO 🔥</h1>"
    return HTML.format(erro="Chave errada")
