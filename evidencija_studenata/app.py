from flask import Flask, render_template, url_for, request, redirect, session 
import mysql.connector

app = Flask(__name__)

#<nav>
@app.route('/studenti', methods=['GET'])
def studenti():
    return render_template('korisnici.html')

@app.route('/predmeti', methods=['GET'])
def predmeti():
    return render_template('korisnici.html')

@app.route('/korisnici', methods=['GET'])
def render_korisnici():
    return render_template('korisnici.html')

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('korisnici.html')
#</nav>

#<table>
@app.route('/korisnik_novi', methods=['GET'])
def korisnik_novi():
    return render_template('korisnici.html')

@app.route('/korisnik_izmena', methods=['GET'])
def korisnik_izmena():
    return render_template('korisnici.html')

@app.route('/korisnik_brisanje', methods=['GET'])
def korisnik_brisanje():
    return render_template('korisnici.html')
#</table>

#login.html
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

app.run(debug=True)
