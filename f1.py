# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def hello():
#     return "hello world"
# app.run(debug=True)

# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def hello():
#     return "welcome to home page"

# @app.route("/about")
# def about():
#     return "welcome to about page"

# @app.route("/contact")
# def contact():
#     return "welcome to contact page"

# app.run(debug=True)

# from flask import Flask
# app=Flask(__name__)

# @app.route("/hello/<name>")
# def hello(name):
#     return "hello mr. "+name
# app.run(debug=True) 

# from flask import Flask,render_template
# app=Flask(__name__)

# @app.route("/hello")
# def hello():
#     return render_template("f1.html")

# app.run(debug=True)

# from flask import Flask,render_template,request
# app=Flask(__name__)

# @app.route("/login",methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         username=request.form["username"]
#         return render_template("f2.html")
#     else:
#         return render_template("f1.html")

# app.run(debug=True)
    
# from flask import Flask,request,render_template
# app=Flask(__name__)

# @app.route("/check",methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         if request.form["name"]=="vatsal":
#             return "Welcome Admin"
#         else:
#             return "Access Denied"
    
#     else:
#         return render_template("f1.html")

# app.run(debug=True)

# from flask import Flask,request,render_template
# app=Flask(__name__)

# @app.route("/login",methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         if request.form["username"]=="vatsal" and request.form["password"]=="123":
#             return render_template("f2.html")
#         else:
#             return "invalid"
#     else:
#         return render_template("f1.html")
        
# app.run(debug=True)


# from flask import Flask,request,render_template

# app=Flask(__name__)

# @app.route("/login",methods=["GET","POST"])

# def login():


#     if request.method=="POST":


#         if request.form["username"]=="vatsal" and int(request.form["password"])=="123":

#             return render_template("f2.html")

#         else:

#             return "invalid"

#     else:

#         return render_template("f1.html")


# app.run(debug=True)


# from flask import Flask,request,render_template
# app=Flask(__name__)

# @app.route("/")

# def info():
#     return render_template("f2.html", name="vatsal", age=21)

# app.run(debug=True)

# from flask import Flask,render_template

# app=Flask(__name__)

# @app.route("/")

# def check():
#     return render_template(
#         "f2.html",
#         name="vatsal",
#         age=21
#     )


# app.run(debug=True)

# import sqlite3


# conn=sqlite3.connect("users.db")

# cursor=conn.cursor()


# cursor.execute(

# "CREATE TABLE IF NOT EXISTS users(name TEXT)"

# )
# cursor.execute(
# "INSERT INTO users VALUES(?)",
# ("vatsal",)
# )
# cursor.execute(
# "SELECT * FROM users"
# )
# cursor.execute(

# "UPDATE users SET name=? WHERE name=?",

# ("patel","vatsal")

# )

# data=cursor.fetchall()
# print(data)

# conn.commit()

# conn.close()

# cursor.execute(
# "DELETE FROM users"
# )

# import sqlite3
# conn=sqlite3.connect("college.db")
# cursor=conn.cursor()
# cursor.execute(
# # "CREATE TABLE students(name TEXT)"
# # )

# # cursor.execute(

# # "INSERT INTO students VALUES(?)",

# # ("vatsal",),

# "INSERT INTO students VALUES(?)",

# ("kasetiya",)

# )

# import sqlite3


# conn=sqlite3.connect("college.db")

# cursor=conn.cursor()


# cursor.execute(

# "DELETE FROM students WHERE name=?",

# ("kasetiya",)

# )
# cursor.execute(

# "DELETE FROM students WHERE name=?",

# ("vatsal",)

# )


# conn.commit()

# conn.close()


# from flask import Flask
# from flask import session


# app=Flask(__name__)

# app.secret_key="123"


# @app.route("/")

# def home():

#     session["city"]="rajkot"

#     return "saved"


# @app.route("/city")

# def show():

#     return session["city"]


# app.run(debug=True)





# from flask import Flask
# from flask import session


# app=Flask(__name__)

# app.secret_key="123"


# @app.route("/")

# def home():

#     session["city"]="rajkot"

#     return "saved"



# @app.route("/city")

# def show():

#     return session["city"]



# @app.route("/logout")

# def logout():

#     session.clear()

#     return "logout success"



# app.run(debug=True)

from flask import Flask
from flask import flash
from flask import render_template


app=Flask(__name__)

app.secret_key="123"


@app.route("/")

def home():

    flash(
    "Login Success"
    )

    return render_template(
    "flash1.html"
    )


app.run(debug=True)
