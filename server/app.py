from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from livros import livros
from filtro import filtrar_livros

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return send_from_directory("../client", "index.html")


@app.route("/api/livros", methods=["GET"])
def listar_livros():
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

    return jsonify(livros_filtrados)


if __name__ == "__main__":
    app.run(debug=True, port=5000)