from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/create")
def create_account():
    return render_template("create_account.html")
