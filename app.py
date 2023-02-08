from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':

        return render_template('home.html')

    else:

        choice = request.form['button']

        # unfortunately `match` is only supported from Python 3.10
        # and this is made using Python 3.9 so if/else statements are used

        if choice == 'Sign up':

            pass

        elif choice == 'Log In':

            return redirect(url_for('login'))

        elif choice == 'Get Started':

            pass

        elif choice == 'Learn More':

            pass

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':

        return render_template('login.html')