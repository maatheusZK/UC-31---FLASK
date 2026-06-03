from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cadastro", methods=["POST"])
def cadastro():

    erros = []

    nome = request.form["nome"].strip().title()
    email = request.form["email"].strip().lower()
    telefone = request.form["telefone"].strip()
    cpf = request.form["cpf"].strip()
    cidade = request.form["cidade"].strip().title()
    estado = request.form["estado"].strip().upper()
    curso = request.form["curso"].strip()
    idade = request.form["idade"].strip()
    senha = request.form["senha"].strip()

    telefone = (
        telefone.replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    cpf = cpf.replace(".", "").replace("-", "")

    if len(nome) < 8:
        erros.append("Nome inválido.")

    if "@" not in email or ".com" not in email:
        erros.append("E-mail inválido.")

    if not telefone.isdigit() or len(telefone) != 11:
        erros.append("Telefone inválido.")

    if not cpf.isdigit() or len(cpf) != 11:
        erros.append("CPF inválido.")

    if len(cidade) < 3:
        erros.append("Cidade inválida.")

    if len(estado) != 2:
        erros.append("Estado inválido.")

    if curso == "":
        erros.append("Curso obrigatório.")

    if not idade.isdigit() or int(idade) < 16:
        erros.append("Idade inválida.")

    possui_numero = any(caractere.isdigit() for caractere in senha)

    if len(senha) < 8 or not possui_numero:
        erros.append("Senha muito fraca.")

    if erros:
        return render_template(
            "resultado.html",
            sucesso=False,
            erros=erros
        )

    return render_template(
        "resultado.html",
        sucesso=True,
        nome=nome,
        email=email,
        telefone=telefone,
        cpf=cpf,
        cidade=cidade,
        estado=estado,
        curso=curso,
        idade=idade
    )


if __name__ == "__main__":
    app.run(debug=True)