"""
***Created by Jeremiah Lantzer and Jonathan Rach for PolyHacks2016
***Credit to Juan for assistance with Flask
***Depends on Flask installation and Twilio messaging API
"""
from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient

"""Set up for Twilio"""
#define account_sid and auth_token and create a TwilioRestClient instance to utilize twilio API
account_sid = "XXX"
auth_token = "XXX"
client = TwilioRestClient(account_sid,auth_token)

#create variable value for phone and variable to track signup message
phone = ""
msgval=0
US = "XXX"

#define initial signup messages to send based on settings clicked in signup
anomsg = "Thank you for signing up for anorexia management reminders. Scheduled eating reminders will proceed at 8:00AM for breakfast, 10:30AM for a morning snack, 12:00PM for lunch, 3:30PM for an afternoon snack, and 7:00PM for dinner."
anxmsg = "Thank you for signing up for anxiety management reminders. Reminders to exercise or perform yoga will occur daily at 6:00AM and reminders to take medicine will occur at 8:00AM and 8:00PM daily."
dmsg = "Thank you for signing up for depression management reminders. Reminders to exercise will occur daily at 6:00AM, reminders to \"love yourself\" will occur daily at 4:00PM, and reminders to take medicine will occur at 8:00AM and 8:00PM daily."

defmsg = "Thank you for signing up for reminder notifications! You will receive reminders at 8:00AM daily for breakfast,  10:30AM daily for a morning snack, 12:00PM daily for lunch, 3:30PM daily for an afternoon snack, and 7:00PM daily for dinner."

"""Begin Flask Implementation"""
#create an instance of Flask
app = Flask(__name__)

""" Set routes for website navigation """
@app.route("/")
def homepage():
    return render_template("index1.html")


@app.route("/login", methods=['GET','POST'],)
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global msgval
    msgval = 1
    return render_template("signup.html")


@app.route("/signup1")
def signup1():
    global msgval
    msgval = 2
    return render_template("signup1.html")


@app.route("/signup2")
def signup2():
    global msgval
    msgval = 3
    return render_template("signup2.html")


@app.route("/index", methods=['GET','POST'])
def index():
    phone = request.form['phone']
    message = client.messages.create(to=("+1"+phone), from_=US, body=amsg)

    return render_template("pages/index.html",phone = request.form['phone'])


@app.route("/indexa")
def indexa():
    phone = request.form['phone']
    message = client.messages.create(to=("+1"+phone), from_=US, body=anxmsg)
    return render_template("pages/indexa.html",phone = request.form['phone'])


@app.route("/indexb")
def indexb():
    phone = request.form['phone']
    message = client.messages.create(to=("+1"+phone), from_=US, body=dmsg)
    return render_template("pages/indexb.html",phone = request.form['phone'])


@app.route("/logged")
def logged_in():
    return render_template("index.html")


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    print msgval
    phone = request.form['phone']
    if msgval == 1:
        message = client.messages.create(to=("+1"+phone), from_=US, body=anomsg)
    elif msgval == 2:
        message = client.messages.create(to=("+1"+phone), from_=US, body=anxmsg)
    elif msgval == 3:
        message = client.messages.create(to=("+1"+phone), from_=US, body=dmsg)
    else:
        message = client.messages.create(to=("+1"+phone), from_=US, body=defmsg)
    return render_template("profile.html",phone = phone)


if __name__ == "__main__":
    app.run()
