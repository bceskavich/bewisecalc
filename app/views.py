from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bac')
def bac():
    return render_template("bac.html")

@app.route('/cups')
def cups():
    return render_template("cups.html")
