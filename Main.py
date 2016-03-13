from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index1.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup1")
def signup1():
    return render_template("signup1.html")


@app.route("/signup2")
def signup2():
    return render_template("signup2.html")


@app.route("/index/<user>")
def index():
    return render_template("pages/index.html")


@app.route("/indexa")
def indexa():
    return render_template("pages/indexa.html")


@app.route("/indexb")
def indexb():
    return render_template("pages/indexb.html")


@app.route("/logged")
def logged_in():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run()
