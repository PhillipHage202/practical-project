from flask import render_template
from application import app, db
from application.models import Char
import requests

@app.route('/', methods=['GET'])
def home():
<<<<<<< HEAD
    return render_template('home.html', title='Home')
=======
    return render_template('index.html', title='Home')
>>>>>>> developer


@app.route('/get_char', methods=['GET'])
def index():
    #gets a wep
    wep = requests.get("http://localhost:5001/wep")
    #gets element
    element = requests.get("http://localhost:5002/element")
    #gets character name
    character = str(wep.text) + "," + str(element.text)
    name = requests.post("http://localhost:5003/name", data=character)

    add_char = Char(wep=wep.text, element=element.text, name=name.text)
    db.session.add(add_char)
    db.session.commit()


<<<<<<< HEAD
    return render_template('index.html', wep=wep.text, element=element.text, name=name.text)
=======
    return render_template('index.html', wep=wep.text, element=element.text, name=name.text)
>>>>>>> developer
