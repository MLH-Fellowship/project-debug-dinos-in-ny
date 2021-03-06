import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *

class Person:
    def __init__(self, f_name, l_name, school, major, hob1, hob2, hob3, hob4):
        self.f_name = f_name
        self.l_name = l_name
        self.school = school
        self.major = major
        self.hob1 = hob1
        self.hob2 = hob2
        self.hob3 = hob3
        self.hob4 = hob4



load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv( "MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv( "MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print (mydb)

sristi = Person("Sristi", "Panchu", "Tufts University", "Computer Science", "crafting (specifically quilling)", "dancing", "reading", "exploring new places")
aima = Person("Aima", "Alakhume", "New York University", "Electrical Engineering", "painting", "writing", "reading", "exploring new places")

@app.route('/')
def index():
    return render_template('index.html', title="Our Portfolios", url=os.getenv("URL"))

@app.route('/aima')
def abaima():
    return render_template('aboutaima.html', student = aima)

@app.route('/sristi')
def absristi():
    return render_template('aboutsristi.html', student = sristi)
