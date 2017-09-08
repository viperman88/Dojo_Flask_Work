from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

Email_Validate = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "This_Is_So_Secret!"
mysql = MySQLConnector(app,'email_val_db')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():

    # Write query as a string
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

    # Create a dictionary of data from the POST data received.
    data = {
        'email': request.form['email']
        }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)

    query = "SELECT * FROM emails"  # define your query
    new_emails = mysql.query_db(query) # run query with query_db()

    errors = False

    if len(request.form['email']) < 1:
        flash('Email cannot be blank!')
        errors = True

    if not Email_Validate.match(request.form['email']):
        flash('Invalid Email Address!')
        errors = True

    if errors is True:
        return redirect('/')

    else:
        flash('The email you entered ' + request.form['email'] + ' is a VALID email address! Thanks!')
        return render_template('success.html', all_emails = new_emails) # pass data to our template

app.run(debug=True)
