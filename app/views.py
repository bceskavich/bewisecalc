from app import app
from flask import render_template, redirect, url_for, flash
from forms import BACForm
from methods import calculate

# Simply returns the index.html template for the intro page.
@app.route('/')
def index():
    return render_template("index.html")

# The Calcuation Page
@app.route('/bac', methods = ['GET', 'POST'])
def bac():
    # Loads the BAC Form file (forms.py) which contains the fields for the calculator
    form = BACForm()
    # When the user submits, data is pulled
    if form.validate_on_submit():
        drinks = {
            'beer': form.beer.data,
            'wine': form.wine.data,
            'liqour': form.liqour.data
        }
        # Form data is inputted to the BAC method, which returns the BAC level
        bac = calculate(drinks, form.weight.data, form.hours.data, form.gender.data)
        # Redirects to the results page with the bac value inputted
        return redirect(url_for('display', bac = bac))
    else:
        flash("Please make sure you input your weight and drinking time--we promise we'll keep it a secret.")
    # Renders the bac.html template when first loaded
    return render_template("bac.html",
        form = form)

# Results page
@app.route('/display/<bac>')
def display(bac):
    # Displays a rounded BAC value
    bac = "%.2f" % round(float(bac),2)
    # Color & Text Warning Ranges
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

    # Scrolling Carousel Content Ranges
    if float(bac) <= .06:
        feels = ['Relaxed', 'More confident', 'Slight euphoria', 'Feeling tipsy', 'Relaxed', 'More talkative', 'Happy']
    elif float(bac) > .06 and float(bac) <= .20:
        feels = ['In control', 'Unstoppable', '"Buzzed"', 'More emotional', 'The room is spinning', 'Groggy, nauseous', 'Uncoordinated', 'Drunk', 'Out of it', 'Over-confident', 'Angry, irrational, jumpy', 'Sick', 'Sleepy', 'Slurring your speech']
    elif float(bac) > .2:
        feels = ['Lost', 'Confused', 'Disoriented', 'Sick', 'Dizzy', 'Exhausted', 'Angry', 'Uncontrollable', 'Unintelligible', 'Unaware', 'Wasted', 'Cannot walk', 'Uncooperative', 'Loss of bladder control', 'Cold skin', 'Unresponsive', 'Puking', 'Slow breathing']

    # Renders results template (display.html) w/ various dynamic features
    return render_template("display.html",
        bac = bac,
        color = color,
        text = text,
        feels = feels,
        length = len(feels))

# Renders the static resources.html page
@app.route('/resources')
def resources():
    return render_template("resources.html")

# Renders the static resources.html page (aka #LastTheNight)
@app.route('/cups')
def cups():
    return render_template("cups.html")
