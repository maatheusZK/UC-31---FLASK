from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "123456"

usuario = ""
senha_hash = ""

@app.route("/", methods=["GET", "POST"])
def cadastro():
    global usuario, senha_hash

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        senha_hash = generate_password_hash(senha)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    global usuario, senha_hash

    mensagem = ""

    if request.method == "POST":
        nome = request.form["usuario"]
        senha = request.form["senha"]

        if nome != usuario:
            mensagem = "Usuário não encontrado."

        elif not check_password_hash(senha_hash, senha):
            mensagem = "Senha incorreta."

        else:
            session["usuario"] = usuario
            return redirect(url_for("inicio"))

    return render_template("login.html", mensagem=mensagem)


@app.route("/inicio")
def inicio():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("inicio.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)