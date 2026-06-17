from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "123456"

@app.route("/")
def inicio():
    return redirect(url_for("contador"))

@app.route("/contador")
def contador():
    if "contador" not in session:
        session["contador"] = 0

    session["contador"] += 1

    return render_template(
        "contador.html",
        acessos=session["contador"]
    )

@app.route("/zerar")
def zerar():
    session.pop("contador", None)
    return redirect(url_for("contador"))

if __name__ == "__main__":
    app.run(debug=True)