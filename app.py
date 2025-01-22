from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    return render_template("hello_there.html", name=name_data)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

 # Replace the existing index function with the one below

 # New functions
@app.route("/about/")
def about():
     return render_template("about.html")

@app.route("/contact/")
def contact():
     return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5421)


