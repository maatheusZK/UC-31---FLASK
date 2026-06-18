from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "123"


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    session["usuario"] = usuario
    session["senha"] = senha

    if "tarefas" not in session:
        session["tarefas"] = []

    return redirect("/tarefas")


@app.route("/tarefas")
def inicio():
    if "usuario" not in session:
        return redirect("/")

    tarefas = session.get("tarefas", [])

    return render_template(
        "index.html",
        usuario=session["usuario"],
        tarefas=tarefas
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefa = request.form["tarefa"]

    tarefas = session.get("tarefas", [])

    tarefas.append({
        "texto": tarefa,
        "feita": False
    })

    session["tarefas"] = tarefas

    return redirect("/tarefas")


@app.route("/marcar/<int:id>")
def marcar(id):
    tarefas = session.get("tarefas", [])

    if 0 <= id < len(tarefas):
        tarefas[id]["feita"] = True

    session["tarefas"] = tarefas

    return redirect("/tarefas")


@app.route("/limpar")
def limpar():
    session.pop("tarefas", None)
    return redirect("/tarefas")


if __name__ == "__main__":
    app.run(debug=True)