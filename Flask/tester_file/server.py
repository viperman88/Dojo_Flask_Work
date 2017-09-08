
from flask import Flask, render_template, redirect, request, session, flash
import datetime
# import re for regular expression
import re
# create a regular expression object for running operations
Email_Validate = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
Pass_Validate = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
# (?=.*?\d) Checks for atleast one digit
# (?=.*?[A-Z]) Atleast one uppercsae.
# (?=.*?[a-z]) Atleast one lowercase.
# [A-Za-z\d]{10,} Matches uppercase or lowercase or digit characters 10 or more
# times. This ensures that the match must have atleast 10 characters

app = Flask(__name__)

app.secret_key = "This_Is_So_Secret!"

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():

    # sets today's date to compare with input date to confirm date is of past
    maxDate = datetime.datetime.today().strftime('%Y-%m-%d')
    print maxDate
    inputDate = request.form['dob']
    print inputDate

    if inputDate == maxDate:
        flash("Invalid date, must be a date from the past!")

    elif len(request.form['email']) < 1:
        flash("Email cannot be blank!")

    elif not Email_Validate.match(request.form['email']):
        flash("Invalid Email Address!")

    elif len(request.form['first_name']) < 1:
        flash("Name cannot be blank!")

    elif len(request.form['last_name']) < 1:
        flash("Name cannot be blank!")

    elif len(request.form['password']) < 1:
        flash("Password cannot be blank!")

    elif not Pass_Validate.match(request.form['password']):
        flash("Password must contain at least 1 digit, 1 uppercase, 1 lowercase, and more than 8 characters!")

    elif request.form['conf_pass'] == request.form['password']:
        flash("Success!")

    else:
        flash("Passwords do not match!")

    return redirect('/')

app.run(debug=True)
