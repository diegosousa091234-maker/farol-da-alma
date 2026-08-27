memorias_db = {}
def salvar_memoria(usuario: str, texto: str):
    if usuario not in memorias_db:
        memorias_db[usuario] = []
    memorias_db[usuario].append({"tipo": "conversa", "texto": texto})
    return True
def buscar_memoria(usuario: str):
    return memorias_db.get(usuario, [])
