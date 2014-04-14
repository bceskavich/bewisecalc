from app import app
from flask import render_template, redirect, url_for
from forms import BACForm
from methods import calculate

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bac', methods = ['GET', 'POST'])
def bac():
    form = BACForm()
    if form.validate_on_submit():
        drinks = {
            'beer': form.beer.data,
            'wine': form.wine.data,
            'liqour': form.liqour.data
        }
        bac = calculate(drinks, form.weight.data, form.hours.data, form.gender.data)
        return redirect(url_for('display', bac = bac))
    return render_template("bac.html",
        form = form)

@app.route('/display/<bac>')
def display(bac):
    return render_template("display.html",
        bac = bac)

@app.route('/cups')
def cups():
    return render_template("cups.html")
