from flask import Flask
from flask import render_template
from flask import request

import sqlite3
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])

def home():

    if request.method=="POST":

        name=request.form["username"]


        conn=sqlite3.connect(
        "galaxy_store.db"
        )

        cursor=conn.cursor()


        cursor.execute(

        "CREATE TABLE IF NOT EXISTS user_records(name TEXT)"

        )


        cursor.execute(

        "INSERT INTO user_records VALUES(?)",

        (name,)

        )


        conn.commit()


        cursor.execute(

        "SELECT * FROM user_records"

        )

        data=cursor.fetchall()


        conn.close()


        return render_template(

        "show.html",

        data=data

        )


    return render_template(
    "input.html"
    )