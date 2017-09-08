
from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def great_numbers():

    if "comp_num" not in session:
        session["comp_num"] = random.randint(0,100)
    print session["comp_num"]

    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def you_lost():
    session["number"] = request.form["num_value"]

    if session["comp_num"] == int(request.form["num_value"]):
        session["outcome"] = "You Won!"
    elif session["comp_num"] > int(request.form["num_value"]):
        session["outcome"] = "Too Low!"
    elif session["comp_num"] < int(request.form["num_value"]):
        session["outcome"] = "Too High!"

    return redirect("/")

@app.route("/refresh", methods=["POST"])
def you_won():

    session.clear()

    return redirect("/")

app.run(debug=True)
