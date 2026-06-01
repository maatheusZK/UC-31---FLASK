from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/inscricao', methods=['GET', 'POST'])
def inscricao():

    mensagem = ""

    if request.method == 'POST':
        nickname = request.form['nickname']
        jogo = request.form['jogo']
        email = request.form['email']

        if len(nickname) < 4 or jogo == "" or email == "":
            mensagem = "Preencha todos os campos obrigatórios."
        else:
            mensagem = "Inscrição realizada com sucesso!"

    return render_template('inscricao.html', mensagem=mensagem)

if __name__ == '__main__':  
    app.run(debug=True)