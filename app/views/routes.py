from flask import render_template,request
from app import app


@app.route('/')
def index():
    titulo = "My Tutorias - HomePage"
    return render_template('index.html',titulo=titulo)

@app.route('/pandas')
def page_pandas():
    titulo = "My Tutorias - Guia pandas"
    return render_template('pandas.html',titulo=titulo)

@app.route('/sqlalchemy')
def page_sqlalchemy():
    titulo = "My Tutorias - Guia sqlalchemy"
    return render_template('sqlalchemy.html',titulo=titulo)

@app.route('/selenium')
def page_selenium():
    titulo = "My Tutorias - Guia sqlalchemy"
    return render_template('selenium.html',titulo=titulo)

@app.route("/contato")
def page_contato():
    titulo = "My Tutorias - Fale com conosco"
    return render_template('contato.html',titulo=titulo)