from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, keep_signed_in={form.keep_signed_in.data}")
        return redirect('/')
    return render_template("login.html", title="Log In", form=form)


@app.route("/create")
def create_account():
    return render_template("create_account.html")
