# Trying out dynamic url 

from flask import Flask 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
    return "Welcome Home"

# Let say i want to welcome the person who has login to teh page page with his name 

@app.route("/Welcome/<name>")
def welcome(name):
    return f"Hi {name.title()}, Welcome to this page."

if __name__ =="__main__":
    app.run(debug=True)

# If while pusjhing your code its showing like the cureent branch is behind use the below code to pull the branch first 
# git pull origin main --rebase and then do push git push -u origin main 


