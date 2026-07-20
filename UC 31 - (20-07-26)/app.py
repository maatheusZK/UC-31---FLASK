from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"

def criar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4, ensure_ascii=False)

def ler_livros():
    criar_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)

@app.route("/", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        if not all([titulo, autor, ano, categoria, quantidade]):
            return "Todos os campos são obrigatórios."

        if not ano.isdigit():
            return "O ano deve conter apenas números."

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return "A quantidade deve ser maior que zero."

        livros = ler_livros()

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        }

        livros.append(livro)
        salvar_livros(livros)

        return redirect(url_for("listar_livros"))

    return render_template("cadastro.html")

@app.route("/livros")
def listar_livros():
    livros = ler_livros()
    return render_template("livros.html", livros=livros)

@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    livro_encontrado = None

    if request.method == "POST":

        titulo = request.form["titulo"].lower()

        livros = ler_livros()

        for livro in livros:
            if livro["titulo"].lower() == titulo:
                livro_encontrado = livro
                break

    return render_template("buscar.html", livro=livro_encontrado)

@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):

    livros = ler_livros()

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        if not all([titulo, autor, ano, categoria, quantidade]):
            return "Todos os campos são obrigatórios."

        if not ano.isdigit():
            return "Ano inválido."

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return "Quantidade inválida."

        livros[indice] = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        }

        salvar_livros(livros)

        return redirect(url_for("listar_livros"))

    return render_template("editar.html", livro=livros[indice], indice=indice)

@app.route("/excluir/<int:indice>")
def excluir(indice):

    livros = ler_livros()

    livros.pop(indice)

    salvar_livros(livros)

    return redirect(url_for("listar_livros"))

if __name__ == "__main__":
    app.run(debug=True)