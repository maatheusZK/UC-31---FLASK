from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('formulario.html')

@app.route('/autenticar', methods=['GET']) 
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return "{} e {}".format(usuario, senha)

if __name__ == '__main__':
    app.run(debug=True)