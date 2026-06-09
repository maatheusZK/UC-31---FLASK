from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = request.cookies.get("nome")
    tema = request.cookies.get("tema", "claro")

    return render_template(
        "index.html",
        nome=nome,
        tema=tema
    )

@app.route("/salvar_nome", methods=["POST"])
def salvar_nome():
    nome = request.form.get("nome")

    resposta = make_response(redirect("/"))
    resposta.set_cookie("nome", nome, max_age=60*60*24*30)

    return resposta

@app.route("/alterar_tema/<tema>")
def alterar_tema(tema):
    resposta = make_response(redirect("/"))
    resposta.set_cookie("tema", tema, max_age=60*60*24*30)

    return resposta

if __name__ == "__main__":
    app.run(debug=True)