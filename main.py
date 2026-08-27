
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
CHAVE_MESTRA = os.getenv("FAROL_KEY", "BrasaSabedoriaforja").strip()

HTML_LOGIN = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TÊMPORA - FAROL DA ALMA</title>
<style>
body { background: #0a0a0a; color: #e8d5a3; font-family: serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin:0; }
.card { background: #111; border: 1px solid #c9a86a; border-radius: 20px; padding: 30px; width: 90%; max-width: 400px; box-shadow: 0 0 30px rgba(201,168,106,0.3); text-align: center; }
h1 { color: #c9a86a; letter-spacing: 4px; margin:0; }
.input-box { position: relative; width: 100%; }
input { width: 90%; padding: 15px; margin: 10px 0; border-radius: 10px; border: 1px solid #c9a86a; background: #000; color: #fff; }
.toggle { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); cursor: pointer; font-size: 20px; user-select: none; }
button { width: 100%; padding: 18px; background: linear-gradient(90deg, #c9a86a, #8a6d3b); border: none; border-radius: 12px; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 20px; }
.pilares { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 25px; font-size: 11px; opacity: 0.8; }
.pilar { border: 1px solid #c9a86a44; padding: 10px; border-radius: 10px; }
</style>
</head>
<body>
<div class="card">
<h1>TÊMPORA</h1>
<p>FAROL DA ALMA</p>
<form method="POST">
<input name="nome" placeholder="Nome do Guerreiro" required>
<div class="input-box">
<input id="chaveInput" name="chave" type="password" placeholder="Chave da Forja" required>
<span class="toggle" onclick="mostrarSenha()">👁️</span>
</div>
<button type="submit">🔥 ACENDER MEU FAROL</button>
</form>
{% if erro %}<p style="color:#ff6b6b; margin-top:15px;">{{erro}}</p>{% endif %}
<div class="pilares">
<div class="pilar">💡 Sabedoria</div>
<div class="pilar">❤️ Coração Estável</div>
<div class="pilar">⛰️ Humildade Forte</div>
<div class="pilar">🛡️ Coragem</div>
</div>
</div>
<script>
function mostrarSenha() {
  var x = document.getElementById("chaveInput");
  if (x.type === "password") { x.type = "text"; } else { x.type = "password"; }
}
</script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        chave = request.form.get("chave","").strip()
        nome = request.form.get("nome","").strip()
        if chave == CHAVE_MESTRA:
            return f"<h1 style='background:#000;color:#c9a86a;text-align:center;padding:50px;'>BEM-VINDO, {nome}! 🔥<br>Farol Aceso!</h1>"
        else:
            return render_template_string(HTML_LOGIN, erro="Chave incorreta!")
    return render_template_string(HTML_LOGIN)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
