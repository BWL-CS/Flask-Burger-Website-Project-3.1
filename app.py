from flask import Flask
from flask import render_template

app = Flask(__name__)

Times = 0

@app.route("/")
def Burger():
    
    global Times 
    Times += 1
    
    return render_template("Burger.html", Times=Times)

@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    
    return render_template("hello_there.html", name=name_data)







@app.route("/Top_Bun/")
def Top_Bun():
     global Times 
     Times += 1
     return render_template("Top_Bun.html", Times=Times)

@app.route("/Sesame/")
def Sesame():
     global Times 
     Times += 1
     return render_template("Sesame.html", Times=Times)

@app.route("/Lettuce/")
def Lettuce():
     global Times 
     Times += 1
     return render_template("Lettuce.html", Times=Times)

@app.route("/Tomato/")
def Tomato():
     global Times 
     Times += 1
     return render_template("Tomato.html", Times=Times)

@app.route("/Cheese/")
def Cheese():
     global Times 
     Times += 1
     return render_template("Cheese.html", Times=Times)

@app.route("/Patty/")
def Patty():
     global Times 
     Times += 1
     return render_template("Patty.html", Times=Times)

@app.route("/Bottom_Bun/")
def Bottom_Bun():
     global Times 
     Times += 1
     return render_template("Bottom_Bun.html", Times=Times)
@app.route("/Me/")
def Me():
     global Times 
     Times = Times * 2
     return render_template("Me.html", Times=Times)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5421, debug=True)


