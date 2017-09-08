from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def survey():
    return render_template("survey.html")

@app.route("/results", methods = ["POST"])
def results():
    #print "Hello"
    #print request.form
    #print request.form["location"]
    return render_template("results.html", user = request.form)

app.run(debug=True)
