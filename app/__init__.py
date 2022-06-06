import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

class Person:
    def __init__(self, f_name, l_name, school):
        self.f_name = f_name
        self.l_name = l_name
        self.school = school



load_dotenv()
app = Flask(__name__)


sristi = Person("Sristi", "Panchu", "Tufts University")
aima = Person("Aima", "Alakhume", "New York University")

@app.route('/')
def index():
    return render_template('index.html', title="Our Portfolio", url=os.getenv("URL"))

@app.route('/aima')
def abaima():
    return render_template('aboutaima.html', student = aima)

@app.route('/sristi')
def absristi():
    return render_template('aboutsristi.html', student = sristi)