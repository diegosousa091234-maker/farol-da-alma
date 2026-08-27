from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
app = FastAPI()
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/imagens", StaticFiles(directory="imagens"), name="imagens")
app.mount("/paginas", StaticFiles(directory="paginas"), name="paginas")
@app.get("/")
def home(): return FileResponse("index.html")
