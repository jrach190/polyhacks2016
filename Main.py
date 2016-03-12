from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index1.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logged-in")
def logged_in():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
