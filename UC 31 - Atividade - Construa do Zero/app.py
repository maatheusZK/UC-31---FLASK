from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "MatheuseRivia"

@app.route('/')
def inicio():
    return render_template("cantinho.html")


@app.route("/cantinho")
def cantinho():
    nome = session.get('usuario_nome')

    # Contador de visitas
    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

    return render_template(
        'cantinho.html',
        nome=nome,
        cor='Azul',
        linguagem='Python',
        frase='Nunca pare de aprender!',
        visitas=visitas
    )


if __name__ == '__main__':
    app.run(debug=True)
