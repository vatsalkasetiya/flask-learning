from flask import Flask
from flask import render_template
from flask import request


app=Flask(__name__)


@app.route("/",methods=["GET","POST"])

def login():

    if request.method=="POST":

        user=request.form["username"]

        password=request.form["password"]


        if user=="vatsal" and password=="123":

            return render_template("home.html")


        else:

            return "Invalid Login"


    return render_template(
    "login.html"
    )


app.run(debug=True)