from flask import Flask, render_template, request, url_for, redirect, session
import random

app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret'

 # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
# random.randrange(0, 101) 
# # random number between 0-100


# session['someKey'] = 50
# Remove something from session like so:
# session.pop('someKey')


@app.route('/')                                                                    
def index():
    # Initialise the counter, or increment it
    if not 'guess' in session:
        session ['guess_number'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])                                                                    
def guess():
    session["guess"] = int(request.form['guess'])
    print session
    return redirect('/')


@app.route('/play_again', methods=['POST'])                                                                    
def play_again():
    session['guess_number'] = random.randrange(0, 101)
    session['guess'] = None
    return redirect('/')
           
app.run(debug=True)