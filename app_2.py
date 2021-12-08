from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now1 = now.strftime("%A, %d %B, %Y at %X")
    formatted_now2 = now.strftime("%a, %d %B, %Y at %X")
    formatted_now3 = now.strftime("%a, %d %b, %Y at %X")
    formatted_now4 = now.strftime("%a, %d %b, %y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now1 + ", and \n" + formatted_now2 + ", and \n" + formatted_now3 + ", and finally" + formatted_now4
    return content