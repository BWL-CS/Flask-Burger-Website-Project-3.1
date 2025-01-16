from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name_data = None):
    return render_template("hello_there", name=name_data)


