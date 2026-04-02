from dicionari import *

def filtrar_livros(livros, titulo=None, autor=None, genero=None, ano=None):
    resultado = livros

    if titulo is not None:
        resultado = [l for l in resultado if l["titulo"] == titulo]

    if autor is not None:
        resultado = [l for l in resultado if l["autor"] == autor]

    if genero is not None:
        resultado = [l for l in resultado if l["genero"] == genero]

    if ano is not None:
        resultado = [l for l in resultado if l["ano"] == ano]

    return resultado