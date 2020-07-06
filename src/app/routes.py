from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, CreateAccountForm


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, keep_signed_in={form.keep_signed_in.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Log In", form=form)


@app.route("/create", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash(f"New account requested for user {form.username.data}, email={form.email.data}")
        return redirect(url_for("login"))
    return render_template("create_account.html", title="Create Account", form=form)
