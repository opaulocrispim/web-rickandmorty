from flask import Flask, render_template, request, redirect, url_for
import json, requests, math
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

busca_realizada = []
paginacao = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    api = requests.get(f'https://drf-rickandmorty-api.herokuapp.com/api/personagem/?page={paginacao[0]}&search={busca_realizada[0]}')
    api = api.json()
    resultados = api['results']
    informacao = math.ceil(api['count']/20)
    return render_template('resultado.html', lista=resultados, info=informacao, paginaAtual=paginacao)

@app.route('/buscar', methods=['POST',])
def buscar():
    busca = request.form['CampoDeBusca']
    busca_realizada.clear()
    busca_realizada.append(busca)
    paginacao.clear()
    paginacao.append(1)
    return redirect(url_for('resultado'))

@app.route('/pagina/<int:num_page>', methods=['POST', 'GET'])
def pagina(num_page):
    paginacao.clear()
    paginacao.append(num_page)
    return redirect(url_for('resultado'))


