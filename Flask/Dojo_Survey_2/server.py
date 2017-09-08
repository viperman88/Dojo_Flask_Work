from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)

app.secret_key = "this is one secret key"

@app.route("/")
def survey():

    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def results():

    errors = False

    if len(request.form['name']) < 1:
        flash("Must input name!")
        errors = True

    if len(request.form['location']) < 1:
        flash("No location selected!")
        errors = True

    if len(request.form['language']) < 1:
        flash("No language selected!")
        errors = True

    if len(request.form['comments']) > 120:
        flash("Comments must not contain more than 120 characters!")
        errors = True

    if errors is True:
        return redirect("/")

    else:
        return render_template("results.html", user = request.form)

app.run(debug=True)
