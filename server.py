from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/ada')
def ada_page():
    return "The ada cohort is the best data science cohort!"

@app.route('/roll-dice')
def roll_dice():
    from random import randint
    dice = randint(1,6)
    return (f"You rolled {dice}! ... Great job!  You're a winner... just like your mom said.")

@app.route('/dumb')
def dumb():
    return "Your mom thinks you're dumb...  my mom thinks you're dumb, too."