def filtrar_livros(livros, titulo="", autor="", genero="", ano=""):
    titulo = titulo.lower().strip()
    autor = autor.lower().strip()
    genero = genero.lower().strip()
    ano = str(ano).strip()

    resultado = []

    for livro in livros:
        if titulo and titulo not in livro["titulo"].lower():
            continue

        if autor and autor not in livro["autor"].lower():
            continue

        if genero and genero not in livro["genero"].lower():
            continue

        if ano and str(livro["ano"]) != ano:
            continue

        resultado.append(livro)

    return resultado