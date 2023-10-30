from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Home, got the /calc/func to run"

@app.route("/calc/square/<x>")
#Square function
def square(x):
    
    return str(int(x) * int(x))

#Sr
@app.route("/calc/multiply/<x>/<y>")
#Multiply Func
def multiply(x,y):
    
    return str(int(x) * int(y))

def sub(x):
    return str(x - 3)
  
def add(x,y):
    return x+y

@app.route("/calc/div/<x>/<y>")
def div(x,y):
    if int(y) == 0:
        return "Undefined (division by zero)"
    return str(int(int(x) / int(y)))
@app.route("/calc/mod/<x>/<y>")
def mod(x, y):
    """Calculate the modulus (remainder) of two numbers."""
    if int(y) == 0:
        return "Cannot divide by zero"
    return str(int(x) % int(y))