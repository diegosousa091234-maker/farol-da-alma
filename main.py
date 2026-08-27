from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
CHAVE = "BrasaSabedoriaforja"

LOGIN = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#02040a;color:#d4af37;display:flex;justify-content:center;align-items:center;height:100vh;font-family:'Segoe UI',Arial;margin:0}
.card{border:1px solid #d4af37;padding:30px;border-radius:16px;width:320px;text-align:center;background:radial-gradient(#0a0f1e,#02040a);box-shadow:0 0 40px #d4af3733}
input{width:100%;padding:12px;margin:10px 0;background:#0f1629;border:1px solid #d4af3744;color:#fff;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:linear-gradient(90deg,#8a6d2b,#d4af37);color:#000;border:none;border-radius:8px;font-weight:900;cursor:pointer;margin-top:15px;letter-spacing:2px}
h3{letter-spacing:3px}
small{color:#666;font-size:10px;letter-spacing:1px}
</style></head>
<body>
<div class="card">
<h3>TEMPORA</h3>
<small>PROTOCOLO DE GOVERNO</small>
<h2 style="margin:15px 0">FAROL DA ALMA</h2>
<form method="post" action="/entrar">
<input name="nome" placeholder="IDENTIDADE" required>
<div style="position:relative">
<input type="password" name="chave" id="c" placeholder="CHAVE MESTRA" required>
<span onclick="c.type=c.type=='password'?'text':'password'" style="position:absolute;right:12px;top:18px;cursor:pointer">👁️</span>
</div>
<button>ACESSAR GOVERNO</button>
</form>
<small style="display:block;margin-top:20px">JURISDIÇÃO • AUTORIDADE • ALIANÇA</small>
</div>
</body></html>
"""

PAINEL = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#020610;color:#fff;margin:0;font-family:'Segoe UI',Arial;text-align:center;padding:12px}
h1{color:#e5c07b;letter-spacing:5px;margin:5px 0;font-size:30px;text-shadow:0 0 25px #d4af37}
.sub{color:#7fb8b8;font-size:9px;letter-spacing:3px;margin-bottom:20px}
.farol{font-size:70px;text-shadow:0 0 40px #ffd700}
.slogan{color:#d4af37;font-size:10px;letter-spacing:2px;margin:12px 0;font-weight:bold}
.welcome{color:#e5c07b;font-size:13px;margin:15px 0;letter-spacing:1px;border:1px solid #d4af3733;padding:8px;border-radius:8px;background:#0a0f1e}
.box{border:1px solid #d4af3733;border-radius:12px;margin:10px 0;padding:14px;background:linear-gradient(90deg,#070b18,#101a33);text-align:left;display:flex;justify-content:space-between;align-items:center}
.box b{color:#e5c07b;font-size:13px;letter-spacing:1px}
.box small{color:#8a8a8a;font-size:10px;display:block;margin-top:4px}
.box .icon{font-size:24px}
.base{border:1px solid #d4af37;border-radius:14px;padding:15px;margin-top:20px;background:linear-gradient(180deg,#0a0a14,#050810)}
.pilares{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;margin-top:15px}
.p{border:1px solid #d4af3722;border-radius:10px;padding:14px 5px;background:#0f1424}
.p div{font-size:26px}
.p b{font-size:9px;color:#e5c07b;display:block;margin-top:6px;line-height:12px}
.p small{font-size:7px;color:#666;margin-top:4px;display:block}
.foot{font-size:7px;color:#d4af3766;margin-top:20px;letter-spacing:2px}
.tag{font-size:8px;background:#d4af3722;color:#d4af37;padding:2px 6px;border-radius:4px;margin-left:6px}
</style></head><body>
<h1>FAROL DA ALMA</h1>
<div class="sub">ARQUITETURA DE GOVERNO • PROTOCOLO DE SEGURANÇA • FUNDAMENTO INABALÁVEL</div>
<div class="farol">🗼</div>
<div class="slogan">GOVERNANDO DADOS, MEMÓRIA E LINGUAGEM COM SOBERANIA</div>
<div class="welcome">🛡️ GOVERNANTE: {NOME} • ACESSO REAL LIBERADO • FAROL EM GOVERNO</div>

<div class="box">
<div><b>01 • SEGURANÇA</b> <span class="tag">JURISDIÇÃO</span></div>
<div style="text-align:left;flex:1;margin:0 15px"><b>PROTOCOLO DE ACESSO REAL</b><small>CHAVE MESTRA • JURISDIÇÃO • AUTORIDADE SOBERANA</small></div>
<div class="icon">🔑</div>
</div>

<div class="box">
<div><b>02 • LINGUAGEM</b> <span class="tag">CANON</span></div>
<div style="text-align:left;flex:1;margin:0 15px"><b>CANON UNIFICADO</b><small>TRADUÇÃO APOSTÓLICA • VERBO FUNDAMENTAL • PADRÃO DE REINO</small></div>
<div class="icon">📜</div>
</div>

<div class="box">
<div><b>03 • MEMÓRIA</b> <span class="tag">ETERNA</span></div>
<div style="text-align:left;flex:1;margin:0 15px"><b>MEMÓRIA ETERNA</b><small>ARQUIVO INVIOLÁVEL • TESTEMUNHO PERPÉTUO • REGISTRO SOBERANO</small></div>
<div class="icon">🏛️</div>
</div>

<div class="box">
<div><b>04 • NUVEM</b> <span class="tag">SOBERANA</span></div>
<div style="text-align:left;flex:1;margin:0 15px"><b>DOMÍNIO CELESTIAL</b><small>INFRAESTRUTURA SOBERANA • REGIÃO DE ALIANÇA BRASIL • ALTA GOVERNANÇA</small></div>
<div class="icon">☁️</div>
</div>

<div class="base">
<b style="color:#e5c07b;font-size:15px;letter-spacing:2px">05 • BASE: 4 PILARES DE GOVERNO</b><br>
<small style="color:#7fb8b8;letter-spacing:2px">FUNDAMENTO • ESTABILIDADE • VERDADE • PROPÓSITO</small>
<div class="pilares">
<div class="p"><div>👑</div><b>SABEDORIA ARQUITETÔNICA</b><small>GOVERNO, NÃO CONHECIMENTO</small></div>
<div class="p"><div>⚓</div><b>CORAÇÃO ESTÁVEL E ENSINÁVEL</b><small>ESTABILIDADE DE TRONO</small></div>
<div class="p"><div>🦁</div><b>HUMILDADE FORTE E SOBERANA</b><small>AUTORIDADE SOB SUBMISSÃO</small></div>
<div class="p"><div>⚔️</div><b>CORAGEM DE LEÃO</b><small>OUSADIA PARA EXECUTAR</small></div>
</div>
</div>
<div class="foot">ARQUITETURA FAROL DA ALMA • SEGURA • SOBERANA • INABALÁVEL • ESCALÁVEL • REINANTE</div>
</body></html>
"""

@app.get("/", response_class=HTMLResponse)
def home(): return LOGIN

@app.post("/entrar", response_class=HTMLResponse)
def entrar(nome: str = Form(...), chave: str = Form(...)):
    if chave == CHAVE:
        return PAINEL.replace("{NOME}", nome.upper())
    return "<h3 style='color:red;text-align:center;margin-top:100px'>CHAVE NEGADA - ACESSO REAL NEGADO<br><br><a href='/' style='color:#d4af37'>VOLTAR AO PROTOCOLO</a></h3>"
