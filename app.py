from flask import Flask, render_template, request
from livros import livros
from filtro import filtrar_livros

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    titulo = request.args.get("titulo", "")
    autor = request.args.get("autor", "")
    genero = request.args.get("genero", "")
    ano = request.args.get("ano", "")

    livros_filtrados = filtrar_livros(
        livros,
        titulo=titulo,
        autor=autor,
        genero=genero,
        ano=ano
    )

    return render_template("index.html", livros=livros_filtrados)


if __name__ == "__main__":
    app.run(debug=True)