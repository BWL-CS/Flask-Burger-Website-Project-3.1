from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def Burger():
    return render_template("Burger.html")

@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    
    return render_template("hello_there.html", name=name_data)







@app.route("/Top_Bun/")
def Top_Bun():
     return render_template("Top_Bun.html")

@app.route("/Sesame/")
def Sesame():
     return render_template("Sesame.html")

@app.route("/Lettuce/")
def Lettuce():
     return render_template("Lettuce.html")

@app.route("/Tomato/")
def Tomato():
     return render_template("Tomato.html")

@app.route("/Cheese/")
def Cheese():
     return render_template("Cheese.html")

@app.route("/Patty/")
def Patty():
     return render_template("Patty.html")

@app.route("/Bottom_Bun/")
def Bottom_Bun():
     return render_template("Bottom_Bun.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5421)


