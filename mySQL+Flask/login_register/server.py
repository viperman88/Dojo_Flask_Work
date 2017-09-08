from flask import Flask,request,redirect,render_template,session,flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
# import re for regular expression

# create a regular expression object for running operations
Email_Validate = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
Pass_Validate = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
# (?=.*?\d) Checks for atleast one digit
# (?=.*?[A-Z]) Atleast one uppercsae.
# (?=.*?[a-z]) Atleast one lowercase.
# [A-Za-z\d]{8,} Matches uppercase or lowercase or digit characters 8 or more
# times. This ensures that the match must have atleast 8 characters

app = Flask(__name__)
mysql = MySQLConnector(app,'login_register')
bcrypt = Bcrypt(app)
app.secret_key = 'some_secret'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    errors = False

    if len(first_name) < 2:
        flash('First name too short')
        errors = True

    if len(last_name) < 2:
        flash('Last name too short')
        errors = True

    if not Email_Validate.match(email):
        flash('Email not valid')
        errors = True

    if len(email) < 1:
        flash('Enter valid email')
        errors = True

    if not Pass_Validate.match(password):
        flash("Password must contain 1 digit, 1 uppercase, 1 lowercase, min 8 characters")
        errors = True

    if request.form['confirm'] != password:
        flash('Password does not match')
        errors = True

    if errors == True:
        return redirect('/')

    else:
        # Query users for existing email address....
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {
            'email': email
        }
        user = mysql.query_db(query,data)
        if len(user) > 0: # we have that email already
            flash('sorry email already taken')
            return redirect('/')
        else:

            # run validations and if they are successful we can create the password hash with bcrypt
            pw_hash = bcrypt.generate_password_hash(password)
            # now we insert the new user into the database
            query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
            data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'pw_hash': pw_hash }
            user_id = mysql.query_db(query, data)
            # render_template to success page
            print user_id
            session['user_id'] = user_id
            return render_template('success.html', first_name = first_name)

@app.route('/login', methods=['post'])
def login():

    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': email }
    user = mysql.query_db(query, data) # user will be returned in a list
    print user # empty list user[0]

    if len(user) > 0:
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            # login user
            session['user_id'] = user[0]['id']
            return render_template('success.html')

        else:
            # set flash error message and redirect to login page
            flash('Incorrect combo of email/password')
            return redirect('/')
    else:
        flash('Incorrect combo of email/password')
        return redirect('/')

app.run(debug=True)
