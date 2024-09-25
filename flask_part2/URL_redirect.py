from flask import Flask 
from flask import redirect # Function to redirect the URL  
from flask import url_for  # This is to take the name of the endpoint and generate url for it 
import time # to provide laps

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
    return "<h1>Welcome Home</h1>"

# Endpoijnt for a passed 
@app.route("/passed")
def passed():
    return "<h1>Congrats!! Your are Passed </h1>"

# Endpoijnt for a failed 
@app.route("/failed")
def failed():
    return f"<h1>Sorry,you are failed</h1>"

# Create an endpoint to take the name and marks input from the user 
@app.route("/score/<name>/<int:Marks>")
def score(name,Marks):
    if Marks<30:
        time.sleep(1)
        return redirect(url_for("failed")) # once we have created this code should have this endpoint to redirect so write that endpoint 
    else:
        time.sleep(1)
        return redirect(url_for("passed")) # saname and marks are given so that we can mention the name into the redirected url
                                                                    # Now the same name and marks should be present into the passed and failed 
if __name__ == "__main__":
    app.run(debug=True )