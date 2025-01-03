from flask import Flask,render_template,redirect,url_for,flash

from form import SignupForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='This_is_the_secret_key'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/signup",methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():  # Once the validation is done and it is correct it will redirect the page to home page 
        flash(f"Successfully registered: ",{form.username.data})
        return redirect(url_for("home"))
    return render_template("signup.html",title="Signup",form= form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Login",form = form)

if __name__ == "__main__":
    app.run(debug=True)