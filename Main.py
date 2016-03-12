from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/<user>")
def homepage():
    return render_template("index1.html")


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/speak")
def speak():
    return render_template("speak.html")


if __name__ == "__main__":
    app.run()
