from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Ada')

@app.route('/ada')
def ada_page():
    return "The ada cohort is the best data science cohort!"

@app.route('/apple')
def apple():
    return "Apples are the best filling for apple pies."

@app.route('/roll-dice')
def roll_dice():
    from random import randint
    dice = randint(1,6)
    return render_template('roll.html', roll=dice)

@app.route('/fancy-math-form')
def fancy_math_form():
    return render_template('fancy-math-form.html')

@app.route('/math-results', methods=['POST'])
def math_results():
    number = request.form['n']
    result = int(number) + 3
    return render_template('math-results.html', result=result)

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']
    greeting = 'Hello, '
    if title != '':
        greeting += title + ' '
    greeting += name + '!'
    return render_template('greeting.html', greeting=greeting)


# @app.route('/roll-dice')
# def roll_dice():
#     from random import randint
#     dice = randint(1,6)
#     return (f"""
#     <h1>You rolled {dice}! ... Great job!  You're a winner... just like your mom said.</h1>
#     """)
