from flask import Flask, send_from_directory
from pathlib import Path
import os

app = Flask(__name__)
ROOT = Path(__file__).parent

@app.route("/")
def home():
    return send_from_directory(ROOT, "index.html")

@app.route("/<path:path>")
def static_files(path):
    # serve css/, js/, paginas/, imagens/ quando você criar
    file_path = ROOT / path
    if file_path.exists() and file_path.is_file():
        return send_from_directory(ROOT, path)
    # se for pasta tipo /paginas/acesso.html
    return send_from_directory(ROOT, path)

@app.route("/health")
def health():
    return {"status": "ok", "farol": "flask aceso"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
