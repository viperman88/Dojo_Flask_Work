
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

def pageVisit():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1

@app.route("/")
def counter_proj():
    pageVisit()
    return render_template("index.html")

@app.route('/ninja')
def ninja2():
    session["counter"] += 1
    # Redirects to the main page
    return redirect("/")

@app.route('/clear')
def resetHacker():
    # Sets the counter back to 1
    session.clear()
    # Redirects to the main page
    return redirect("/")

app.run(debug=True)
