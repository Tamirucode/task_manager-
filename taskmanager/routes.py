from flask import render_template, url_for
from taskmanager import app, db
from taskmanager.models import User, Admindata, Tabledata


@app.route("/")
def home():
    return render_template("signup.html")