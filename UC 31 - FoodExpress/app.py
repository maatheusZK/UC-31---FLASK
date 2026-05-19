from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


@app.route("/pedido")
def pedidos():
    return render_template("pedido.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/lanche/<nome>")
def lanche(nome):

    return render_template(
        "lanche.html",
        nome=nome
    )


@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade
    )

if __name__ == "__main__":
    app.run(debug=True)