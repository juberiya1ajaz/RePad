from flask  import Flask , redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from cs50 import SQL
from flask_sqlalchemy import SQLAlchemy

# Configure application

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQL("sqlite:///user.db")
# Ensure responses aren't cached

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')

def index():    
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""
    if request.method == "POST":
        if not request.form.get("username"):
            return "must provide username"
        elif not request.form.get("password"):
            return "must provide password"
       
        return redirect("/")
    else:
        return render_template("login.html")
    
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name= request.form.get("f_name")
        last_name= request.form.get("l_name")
        user = request.form.get("user")
        role = request.form.get("role")
        message = request.form['text']

        # Ensure username was submitted
        if not first_name or not last_name :
            return ("Please provide your name", 403)

        # Ensure necessary data was submitted
        elif not user:
            return ("please provide data", 403)
        elif not role:
            return ("please provide current role", 403)
        elif not message:
            return ("please provide some comments", 403)


        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("form.html")


    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password=request.form.get("password")
        c_password=request.form.get("confirmation")
        #show apology if some error was occured
        if not username:
            return "must provide username"
        elif not password or not  c_password :
            return"must provide password" 
        return redirect("/")
    else:
        return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)

