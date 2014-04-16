from app import app
from flask import render_template, redirect, url_for, flash
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
    else:
        flash("Please make sure you input your weight and drinking time--we promise we'll keep it a secret.")
    return render_template("bac.html",
        form = form)

@app.route('/display/<bac>')
def display(bac):
    bac = "%.2f" % round(float(bac),2)
    if float(bac) < .08:
        color = '#a1facd'
        text = "You're starting to feel relaxed and a little light headed. You'll notice yourself feeling a little more outgoing and talking louder. Be careful as it's still early and you're in a good place."
    elif float (bac) >= .08 and float(bac) < .1:
        color = '#f1f99b'
        text = "You've reached the legal point of intoxication in New York. Don't drive, and be careful: you're beginning to get quite intoxicated."
    elif float(bac) >= .1 and float(bac) < .16:
        color = '#f1f99b'
        text = "You're at a high point of intoxication: your motor skills and coordination are most likely now impaired. You should stop drinking now and figure out a way to get home safely."
    elif float(bac) >= .16 and float(bac) < .2:
        color = '#f1f99b'
        text = "You're beginning to reach a critical, harmful point of intoxication. Your memory is impaired and you will most likely forget much of the evening. The alcohol in your body is now supressing your gag reflex as well. You should think about contacting medical assistance."
    elif float(bac) >= .2:
        color = '#fc96a5'
        text = "Your BAC is too high! Seek immediate medical attention!"
    return render_template("display.html",
        bac = bac,
        color = color,
        text = text)

@app.route('/resources')
def resources():
    return 'Hi!'

@app.route('/cups')
def cups():
    return render_template("cups.html")
