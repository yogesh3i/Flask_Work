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

# Trying out dynamic url 

from flask import Flask,render_template,url_for # used to navigate 
from employee import employee_data
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html",title="Home Page")

# Let say i want to welcome the person who has login to teh page page with his name 

@app.route("/About/<name>")
def About(name):
    return  render_template("about.html",title1="About Page")

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",title="Evaluate",number=num)

@app.route("/employee")
def employee():
    return render_template("employee.html",
                            title="Employee",
                            emps=employee_data)

@app.route("/employee/manager")
def manager():
    return render_template("manager.html",
                            title='Manager',
                            emps=employee_data)
    


if __name__ =="__main__":
    app.run(debug=True)



# If while pusjhing your code its showing like the cureent branch is behind use the below code to pull the branch first 
# git pull origin main --rebase and then do push git push -u origin main 

