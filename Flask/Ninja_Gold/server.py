from flask import Flask, render_template, request, redirect,session
import random,datetime

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():

    if "my_gold" not in session:
        session["my_gold"] = 0
        session["activities"] = []
    print session # allows me to view my session to make sure not empty with error!

    return render_template("index.html")

@app.route("/process_money", methods=["post"])
def money():

    date = datetime.datetime.now().strftime("%Y/%m/%d %X %p")
    print date # make sure date is correct, full year/mon/day, local time, am/pm

    if request.form["building"] == "Farm":
        gold = random.randint(10,20)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + " golds from the farm! (" + date + ")")

    elif request.form["building"] == "Cave":
        gold = random.randint(5,10)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + " golds from the cave! (" + date + ")")

    elif request.form["building"] == "House":
        gold = random.randint(2,5)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + " golds from the house! (" + date + ")")

    elif request.form["building"] == "Casino":
        gold = random.randint(-50,50)
        session["my_gold"] += gold
        if gold > 0:
            session["activities"].append("You earned " + str(gold) + " golds from the casino! (" + date + ")")
        else:
            session["activities"].append("You lost " + str(gold) + " golds from the casino! (" + date + ")")

    return redirect("/")

@app.route("/refresh", methods=["POST"])
def you_won():

    session.clear()
    return redirect("/")

app.run(debug=True)
