
import sys, base64, os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
CHAVE_MESTRA = "BrasaSabedoriaforja"

# Pega a imagem que você passa no comando
IMAGEM_BASE64 = ""
if len(sys.argv) > 1:
    caminho_imagem = sys.argv[1]
    if os.path.exists(caminho_imagem):
        with open(caminho_imagem, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            ext = caminho_imagem.split('.')[-1]
            IMAGEM_BASE64 = f"data:image/{ext};base64,{b64}"
            print(f"✅ IMAGEM CARREGADA: {caminho_imagem}")
    else:
        print(f"❌ Imagem não encontrada: {caminho_imagem}")

LOGIN = f"""
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{{background:#020a1a;color:#f0d27a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;font-family:Arial}}
.card{{border:1px solid #c8a44a;padding:30px;border-radius:14px;width:340px;text-align:center;background:radial-gradient(#0d1933,#020a1a);box-shadow:0 0 60px #c8a44a33}}
input{{width:100%;padding:13px;margin:8px 0;background:#0a1430;border:1px solid #c8a44a55;color:#fff;border-radius:8px;box-sizing:border-box}}
button{{width:100%;padding:14px;background:linear-gradient(90deg,#8a6d2b,#f0d27a);color:#000;border:none;border-radius:8px;font-weight:900;cursor:pointer;letter-spacing:2px;margin-top:10px}}
</style></head>
<body>
<div class="card">
<h3 style="letter-spacing:5px;margin:0">FAROL DA ALMA</h3>
<small style="color:#7fa6a6;letter-spacing:2px">PROTOCOLO DE GOVERNO</small>
<h4 style="margin:20px 0 5px">TEMPORA • 01 SEGURANÇA</h4>
<form method="post" action="/entrar">
<input name="nome" placeholder="IDENTIDADE" required>
<input type="password" name="chave" placeholder="Chave Mestra + Usuários" required>
<button>ACESSAR FAROL</button>
</form>
</div>
</body></html>
"""

DIAGRAMA_HTML = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#020a1e;color:#fff;margin:0;font-family:Arial;text-align:center;padding:10px}
.titulo{color:#f1d07a;font-size:28px;font-weight:900;margin:15px 0 5px}
.sub{color:#8db0b0;font-size:9px;letter-spacing:3px}
.img-box{max-width:700px;margin:20px auto;border:2px solid #c9a84c;border-radius:16px;overflow:hidden;box-shadow:0 0 40px #c9a84c55}
.img-box img{width:100%;display:block}
.welcome{max-width:700px;margin:15px auto;border:1px solid #c9a84c33;background:#0a1430;padding:10px;border-radius:8px;color:#f1d07a}
</style></head>
<body>
<div class="titulo">FAROL DA ALMA</div>
<div class="sub">DIAGRAMA ARQUITETÔNICO • DESIGN MODERNO E ESPIRITUAL</div>
<div class="welcome">🛡️ GOVERNANTE: {NOME} • ACESSO LIBERADO • 01 SEGURANÇA</div>
<div class="img-box">
<img src="{IMAGEM}" alt="Farol da Alma">
</div>
<div style="font-size:8px;color:#c9a84c55;letter-spacing:2px;margin-top:15px">ARQUITETURA FAROL DA ALMA • SEGURA • CONFIÁVEL • ESPIRITUAL • ESCALÁVEL</div>
</body></html>
"""

@app.get("/", response_class=HTMLResponse)
def home(): return LOGIN

@app.post("/entrar", response_class=HTMLResponse)
def entrar(nome: str = Form(...), chave: str = Form(...)):
    if chave == CHAVE_MESTRA:
        img_src = IMAGEM_BASE64 if IMAGEM_BASE64 else "https://via.placeholder.com/700x1000/020a1e/c9a84c?text=FAROL+DA+ALMA"
        return DIAGRAMA_HTML.replace("{NOME}", nome.upper()).replace("{IMAGEM}", img_src)
    return "<h2 style='color:red;text-align:center;margin-top:100px'>CHAVE NEGADA<br><a href='/'>VOLTAR</a></h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
