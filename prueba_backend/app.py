from flask import Flask, render_template
from src.request import search_to_name  

app = Flask(__name__)

@app.route('/')
def index():
    results = search_to_name('bleach')
    data = results['data'] 
    return render_template("index.html", data=data)  

if __name__ == '__main__':
    app.run(debug=True)
