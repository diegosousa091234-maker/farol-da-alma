from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn, os, base64
from pathlib import Path

# importa o efeito que você criou
from queimador import aplicar_queimadura, detectar_formato

app = FastAPI()
CHAVE_MESTRA = "BrasaSabedoriaforja"

# Procura uma imagem na pasta pra queimar
def achar_imagem_base():
    pasta = Path(".")
    for ext in ["*.jpg", "*.jpeg", "*.png", "*.webp", "*.JPG", "*.PNG"]:
        for arq in pasta.glob(ext):
            if "queimado" not in arq.name and arq.name != "farol_da_alma_diagrama.webp":
                return arq
    return None

def gerar_base64_queimado():
    img_path = achar_imagem_base()
    if not img_path:
        return ""
    fmt, size, mode = detectar_formato(img_path)
    print(f"📖 Imagem base detectada: {img_path} {fmt} {size}")
    try:
        from PIL import Image
        with Image.open(img_path) as img:
            queimada = aplicar_queimadura(img)
            # salva _queimado no mesmo diretório
            saida = img_path.parent / f"{img_path.stem}_queimado{img_path.suffix}"
            queimada.save(saida, quality=95)
            print(f"✅ Salvo: {saida}")
            # converte pra base64 pra exibir no site
            import io
            buf = io.BytesIO()
            queimada.save(buf, format="JPEG", quality=90)
            b64 = base64.b64encode(buf.getvalue()).decode()
            return f"data:image/jpeg;base64,{b64}"
    except Exception as e:
        print(f"❌ Erro: {e}")
        return ""

IMAGEM_QUEIMADA_B64 = gerar_base64_queimado()

LOGIN = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{background:#020a1e;color:#d4af37;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;font-family:Arial}
.card{border:1px solid #d4af37;padding:28px;border-radius:14px;width:330px;text-align:center;background:#0a1430}
input{width:100%;padding:12px;margin:6px 0;background:#06102a;border:1px solid #d4af3766;color:#fff;border-radius:8px}
button{width:100%;padding:13px;background:linear-gradient(90deg,#8a6d2b,#f0d27a);border:none;border-radius:8px;font-weight:900;letter-spacing:2px;cursor:pointer;margin-top:8px}
</style></head>
<body><div class="card"><h3 style="letter-spacing:4px">FAROL DA ALMA</h3><small>01 • SEGURANÇA - Chave Mestra + Usuários</small>
<form method="post" action="/entrar" style="margin-top:15px"><input name="nome" placeholder="IDENTIDADE" required><input name="chave" type="password" placeholder="Chave Mestra + Usuários" required><button>ACESSAR FAROL</button></form></div></body></html>
"""

@app.get("/", response_class=HTMLResponse)
def home(): return LOGIN

@app.post("/entrar", response_class=HTMLResponse)
def entrar(nome: str = Form(...), chave: str = Form(...)):
    if chave != CHAVE_MESTRA:
        return '<h2 style="color:red;text-align:center;margin-top:100px">CHAVE NEGADA<br><a href="/">VOLTAR</a></h2>'
    img_tag = f'<img src="{IMAGEM_QUEIMADA_B64}" style="width:100%;max-width:680px;border:2px solid #d4af37;border-radius:14px;box-shadow:0 0 35px #d4af3755">' if IMAGEM_QUEIMADA_B64 else '<div style="font-size:70px">🗼</div>'
    return f"""
    <html><head><meta name="viewport" content="width=device-width,initial-scale=1"></head>
    <body style="background:#020a1e;color:#fff;text-align:center;font-family:Arial;padding:15px">
    <h2 style="color:#d4af37;letter-spacing:3px">FAROL DA ALMA</h2>
    <p style="color:#d4af37">GOVERNANTE: {nome.upper()} • 01 SEGURANÇA LIBERADA • Firme na frequência ✅</p>
    <div style="max-width:700px;margin:20px auto">{img_tag}</div>
    <p style="font-size:8px;color:#d4af3766;letter-spacing:2px;margin-top:20px">ARQUITETURA FAROL DA ALMA • SEGURA • CONFIÁVEL • ESPIRITUAL • ESCALÁVEL • _queimado</p>
    </body></html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
