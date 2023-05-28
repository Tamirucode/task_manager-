from flask import render_template, url_for
from taskmanager import app, db
from taskmanager.models import Admindata, Userdata, Tabledata



@app.route("/")
def home():
    return render_template("signup.html")