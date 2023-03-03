import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        del_name = request.form.get("del_name")

        # Here controlling inputs if there is empty one
        if not request.form.get("name") or not request.form.get("month") or not request.form.get("day"):
            # Deleting name 
            if request.form.get("del_name"):
                db.execute("DELETE FROM birthdays WHERE name = ?", del_name)
                return redirect("/")
            else:
                return redirect("/")
        else:
            db.execute("INSERT INTO birthdays (name,month,day) VALUES(?, ?, ?)", name, month, day)
            return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)

