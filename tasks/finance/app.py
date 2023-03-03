import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    result = db.execute("SELECT name, symbol, price, SUM(shares) as sumShares FROM history WHERE user_id = ? GROUP BY symbol", user_id )
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cashed = cash[0]["cash"]
    pocket = cashed

    for item in result:
        cashed += item["price"] * item["sumShares"]

    return render_template("index.html", result=result, cashed=cashed, usd=usd, pocket=pocket )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        #Getting inputs from form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        stock = lookup(symbol)

        #Input Validation
        if not symbol:
            return apology("Please give a symbol")

        elif not stock:
            return apology("Symbol not founded")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares should be a integer!")

        if shares <= 0:
            return apology("Shares cannot be negativ")
        #User validation
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = cash[0]["cash"]
        #Counting share value
        transaction = shares * stock["price"]
        date = datetime.datetime.now()
        typ = "Buy"

        if user_cash < transaction:
            return apology("Not enough money")

        else:
            #Adding changes for buying
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - transaction, user_id)
            db.execute("INSERT INTO history (user_id, name, price, shares, symbol, time, type) VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, stock["name"],  stock["price"], shares, stock["symbol"], date, typ)
            flash("Thanks for buy!")
            return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    #Calling items from
    history_db = db.execute("SELECT type, name, symbol, shares, price, time FROM history WHERE user_id = ?", user_id)
    return render_template("history.html", history_db=history_db, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        symbol = request.form.get("symbol")
        stock = lookup(symbol)

        if not symbol:
            return apology("Please enter symbol")

        elif not stock:
            return apology("There is no Symbol")
        else:
            return render_template("quoted.html", stock=stock, usd=usd)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Define variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Please enter a username")
        elif not password:
            return apology("Please enter a password")
        elif not confirmation:
            return apology("Please enter both of passwords")

        # Checking Passwords
        elif password == confirmation:
            try:
                # Generating hash and inserting to DB (if username also valid)
                hash = generate_password_hash(password)
                db.execute("INSERT INTO users (username,hash) VALUES(?, ?)",username, hash)
                return redirect("/")
            except:
                return apology("Please try another username")
        else:
            return apology("Passwords dosent match")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "GET":
        bought_symbol = db.execute("SELECT symbol FROM history WHERE user_id = ? GROUP BY symbol", user_id)

        return render_template("sell.html", bought_symbol=bought_symbol)

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("Please type a symbol")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares can't negative")
        # Calling API
        share_name = lookup(symbol)["name"]
        share_price = lookup(symbol)["price"]
        # Counting selling price
        sell_price = shares * share_price

        shares_bought = db.execute("SELECT shares FROM history WHERE user_id = ? and symbol = ? GROUP BY symbol", user_id, symbol)
        shares_bought = shares_bought[0]["shares"]

        if shares_bought < shares:
            return apology("You don'h have enough shares")

        typ = "SOLD"

        update_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        update_cash = update_cash[0]["cash"]
        # Getting back after sell money and share
        money_back = db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash + sell_price, user_id)
        share_back = db.execute("INSERT INTO history (user_id, name, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?, ?)", user_id, share_name, symbol, -shares, share_price, typ)

        flash("Sale Successful")
        return redirect("/")

    return apology("sell.html")