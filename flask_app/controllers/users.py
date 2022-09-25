from crypt import methods
from flask_app import app
from flask import request, redirect, session, render_template

@app.route("/")
def login_reg_page():
    return render_template("home_page.html")

@app.route('/login', methods=['post'])
def login():
    session['user_name'] = request.form['user_name']
    return redirect('/cities')