from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/user/<string:username>")
def greet_user(username):
    return f"Hola, {username}! Bienvenido a Flask."


@app.route('/')
def index():
    return render_template("index.html", nombre="ivana" )
3


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return f"¡Hola, {name}! Tu formulario fue enviado correctamente."



if __name__ == '__main__':
    app.run(debug=True)
