# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def home():
#     print("home")

# @app.route("/about")
# def about():
#     return "about"

# @app.route("/contact")
# def contact():
#     return "contact"

# app.run(debug=True)

# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def home():
#     return "welcome to flask"

# @app.route("/about")
# def about():
#     return "my name is vatsal"

# @app.route("/contact")
# def contact():
#     return "9898113923"

# app.run(debug=True)

# from flask import Flask


# app=Flask(__name__)


# @app.route("/hello/<name>")

# def hello(name):

#     return "Hello " + name


# app.run(debug=True)

# from flask import Flask
# app=Flask(__name__)

# @app.route("/hello/<name>")
# def hello(name):
#     return "hello" + name

# app.run(debug=True)

# from flask import Flask
# from flask import render_template


# app=Flask(__name__)


# @app.route("/")

# def home():

#     return render_template("home.html")


# app.run(debug=True)

# from flask import Flask
# from flask import render_template

# app=Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html",name="hello vatsal")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# app.run(debug=True)

# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route("/login", methods=["GET", "POST"])
# def login():

#     if request.method == "POST":

#         username = request.form["username"]

#         password = request.form["password"]

#         return f"Hello {username}"


#     return render_template("login.html")


# app.run(debug=True)

# from flask import Flask,render_template,request
# app=Flask(__name__)

# @app.route("/welcome",methods=["get","post"])

# def welcome():
#     if request.method=="POST":
#         name=request.form["name"]
#         return "weclome "+name
    
  
#     return render_template("login.html")

# app.run(debug=True)


# from flask import Flask,render_template,request

# app=Flask(__name__)

# @app.route("/age",methods=["GET","POST"])

# def check():
#      if request.method=="POST":
#           age=int(request.form["age"])
          
#           if (age>=18):
#                return "Access Granted"
#           else:
#                return "Access Denied"
               
#      return render_template("age.html")

# app.run(debug=True)

# from flask import Flask
# from flask import render_template
# from flask import request
# from flask import redirect
# from flask import url_for
# app=Flask(__name__)

# @app.route("/home")
# def home():
#      return "login sucess"

# @app.route("/login",methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#          username=request.form["username"]
#          password=request.form["password"]

#          if(username=="vatsal" and password=="123"):
#               return redirect(url_for("home"))
#          else:
#               return "try again"
    
#     return render_template("login.html")

# app.run(debug=True)

        
       

# from flask import Flask
# from flask import render_template


# app=Flask(__name__)


# @app.route("/")

# def home():

#     return render_template("home.html")


# from flask import Flask
# from flask import render_template





# from flask import Flask
# from flask import render_template

# app=Flask(__name__)


# @app.route("/profile")

# def home():

#     return render_template("profile.html")

# app.run(debug=True)

# from flask import Flask,request
# from flask import render_template


# app=Flask(__name__)



# @app.route("/login",methods=["GET","POST"])

# if request.method=="POST":
#     def user():
#         return render_template(
#          "age.html",
#             age=21
#         )


# app.run(debug=True)