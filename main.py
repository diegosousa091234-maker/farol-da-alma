
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

CHAVE_MESTRA = "BrasaSabedoriaforja"

LOGIN_HTML = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#000;color:#d4af37;display:flex;justify-content:center;align-items:center;height:100vh;font-family:Arial;margin:0}
.card{border:1px solid #d4af37;padding:25px;border-radius:12px;width:300px;text-align:center;background:#0a0a0a;box-shadow:0 0 20px #d4af3755}
input{width:100%;padding:10px;margin:8px 0;background:#222;border:1px solid #444;color:#fff;border-radius:6px}
button{width:100%;padding:12px;background:#8a6d2b;color:#fff;border:none;border-radius:6px;font-weight:bold;cursor:pointer;margin-top:10px}
h3{letter-spacing:2px}
</style></head><body>
<div class="card">
<h3>TEMPORA - FAROL DA ALMA</h3>
<form method="post" action="/entrar">
<input name="nome" placeholder="Nome" required>
<div style="position:relative"><input type="password" name="chave" id="ch" placeholder="Chave" required><span onclick="ch.type=ch.type=='password'?'text':'password'" style="position:absolute;right:10px;top:12px;cursor:pointer">👁️</span></div>
<button>ACENDER MEU FAROL</button>
</form></div></body></html>
"""

DASHBOARD_HTML = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#000;color:#fff;margin:0;font-family:Arial}
.header{text-align:center;padding:15px;color:#d4af37;font-size:22px;font-weight:bold;text-shadow:0 0 10px #d4af37;letter-spacing:3px}
.farol{text-align:center;font-size:80px;margin:10px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px}
.box{border:1px solid #d4af37;border-radius:10px;padding:12px;background:#111}
.box h4{margin:0;color:#d4af37}
.box p{font-size:12px;color:#ccc;margin:5px 0 0 0}
.base{margin:10px;border:1px solid #d4af37;border-radius:10px;padding:10px;background:#0a0a0a;text-align:center}
.pilares{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;margin-top:10px}
.pilar{border-left:1px solid #d4af3733;padding:5px}
.pilar b{color:#d4af37;font-size:12px;display:block}
.pilar span{font-size:10px;color:#aaa}
.welcome{text-align:center;padding:10px;color:#d4af37}
</style></head><body>
<div class="header">FAROL DA ALMA</div>
<div class="welcome">BEM-VINDO {NOME}! FAROL ACESO 🔥</div>
<div class="farol">🗼</div>
<div class="grid">
<div class="box"><h4>01 🔒 SEGURANÇA</h4><p>Proteção dos dados<br>• Ética e confiança<br>• Salvaguarda espiritual</p></div>
<div class="box"><h4>02 💬 LINGUAGEM</h4><p>• Comunicação clara<br>• Empatia no diálogo<br>• Tradução da verdade</p></div>
<div class="box"><h4>03 🧠 MEMÓRIA</h4><p>Lembras com sabedoria<br>• Registro consciente<br>• Histórias que guiam</p></div>
<div class="box"><h4>04 ☁️ NUVEM</h4><p>Armazenamento seguro<br>• Conexão elevada<br>• Acesso em todo lugar</p></div>
</div>
<div class="base">
<h4 style="color:#d4af37;margin:0">05 BASE: 4 PILARES</h4>
<div class="pilares">
<div class="pilar"><b>Sabedoria</b><span>Discernimento e conhecimento</span></div>
<div class="pilar"><b>Coração Estável</b><span>Equilíbrio e serenidade</span></div>
<div class="pilar"><b>Humildade Forte</b><span>Força na simplicidade</span></div>
<div class="pilar"><b>Coragem</b><span>Ação com integridade</span></div>
</div>
</div>
</body></html>
"""

@app.get("/", response_class=HTMLResponse)
def home(): return LOGIN_HTML

@app.post("/entrar", response_class=HTMLResponse)
def entrar(nome: str = Form(...), chave: str = Form(...)):
    if chave == CHAVE_MESTRA:
        return DASHBOARD_HTML.replace("{NOME}", nome.upper())
    return "<h3 style='color:red;text-align:center;margin-top:50px'>CHAVE INVÁLIDA<br><a href='/'>voltar</a></h3>"
