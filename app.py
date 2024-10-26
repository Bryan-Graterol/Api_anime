from flask import Flask, redirect, render_template, url_for
import requests
from src.request import search_to_name
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    results = search_to_name('boruto')
    data = results['data'] 
    return render_template("index.html", data=data)

@app.route('/search/')
def search():
    query = request.args.get('name_anime')
    if not query:
        return redirect(url_for('index'))
    # Realiza la búsqueda usando la API de Jikan
    endpoint = f"https://api.jikan.moe/v4/anime?q={query}&sfw"
    response = requests.get(endpoint)
    results = response.json().get("data", [])  # Obtiene los datos de anime encontrados

    # Renderiza la plantilla con los resultados de la búsqueda
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run()
