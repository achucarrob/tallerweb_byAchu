from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/saludo")
def saludo():
    return render_template("index.html")

@app.route("/tarjeta")
def tarjeta():
    nombre = 'Pablo'
    especie = 'Backyardigan'
    return render_template ('tarjeta_con_jinja.html', nombre = nombre , especie = especie)

@app.route("/personaje")
def personaje():
    # Definimos la url a la que se hace el pedido 
    url = 'https://rickandmortyapi.com/api/character/4'
    
    # Hacemos el pedido a la API -- nos devuelve un diccionario
    respuesta_api = requests.get(url).json()

    # Creamos variables a traves de acceder la respuesta
    nombre = respuesta_api['name']
    estado = respuesta_api["status"]
    imagen = respuesta_api['image']

    return render_template('personaje.html', nombre=nombre, estado=estado, imagen=imagen)

@app.route("/personajes")
def todos_los_personajes():

    url = 'https://rickandmortyapi.com/api/character'

    respuesta = requests.get(url).json()

    lista_de_personajes = respuesta ['results']

    return render_template('rick_and_morty.html', lista_de_personajes = lista_de_personajes)