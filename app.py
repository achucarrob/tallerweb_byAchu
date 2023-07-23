from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola, mundo!"

@app.route("/hapi")
def tarjeta():
    return render_template ('tarjeta.html')