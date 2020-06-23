from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/create")
def create_account():
    return render_template("create_account.html")


if __name__ == "__main__":
    app.run()
