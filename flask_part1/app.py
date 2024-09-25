from flask import Flask 

app = Flask(__name__)  # This is the main instance of the app 

# Creating home page 
@app.route("/")    # This is the modules of the app 
@app.route("/home")
def home(): # this is nothing but a functionality of the app in specific tab waht is doing.
    return "Hello World"

# Creating about page 
@app.route("/About")
def about():
    return "Welcome to the about Page"

# Get the user name and display his name on the 

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name.title()} welcome Here !!"

# Taking one number and try adding it to 10 

@app.route("/addi/<int:num1>")
def add(num1):
    return f"The addition is {num1+10}"

# Take 2 numbers and add them 

@app.route("/Addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"Summation of this 2 numbers is {num1+num2}"

if __name__ == "__main__":
    app.run(debug=True)