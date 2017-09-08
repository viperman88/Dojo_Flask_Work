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
mysql = MySQLConnector(app,'The_Wall')
bcrypt = Bcrypt(app)
app.secret_key = 'some_secret'

@app.route('/')
def index():

    '''if session['user_id'] > 0:
        flash('User is looged in, logout to go to Login/Registration')
        return redirect('/wall')

    else:'''
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
        data = {'email': email}
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
            # render_template to wall page
            print user_id
            session['user_id'] = user_id
            session['user'] = first_name
            flash('SUCCESSFUL REGISTRATION Welcome to The Wall')
            return redirect('/wall')

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
            session['user'] = user[0]['first_name']
            flash('SUCCESSFUL LOGIN Welcome to The Wall')
            return redirect('/wall')

        else:
            # set flash error message and redirect to login page
            flash('Incorrect combo of email/password')
            return redirect('/')
    else:
        flash('Incorrect combo of email/password')
        return redirect('/')

@app.route('/wall')
def wall():

    query = 'SELECT users.first_name, users.last_name, messages.user_id, messages.messages, DATE_FORMAT(messages.created_at, " %M %d, %Y ") AS created_date, messages.id FROM messages JOIN users ON users.id = messages.user_id ORDER BY created_date DESC;'
    comment_query = 'SELECT users.first_name, users.last_name, comments.comments, DATE_FORMAT(comments.created_at, " %M %d, %Y ") AS created_date, comments.id, comments.user_id, comments.message_id FROM comments INNER JOIN users ON users.id = comments.user_id INNER JOIN messages ON messages.id = comments.message_id;'
    comments = mysql.query_db(comment_query)
    messages = mysql.query_db(query)

    return render_template('success.html', messages=messages, comments=comments)

@app.route('/post_message', methods=['post'])
def message():

    data = {
            'user_session': session['user_id'],
            'user_message': request.form['add_message']
            }
    query = 'INSERT INTO messages (user_id, messages, created_at, updated_at) VALUES (:user_session, :user_message, NOW(), NOW())'
    mysql.query_db(query,data)

    return redirect('/wall')

@app.route('/post_comment/<id>', methods=['post'])
def comment(id):

    data = {
            'exact_id': id,
            'user_session': session['user_id'],
            'user_comment': request.form['add_comment']
            }
    query = 'INSERT INTO comments (user_id, message_id, comments, created_at, updated_at) VALUES (:user_session, :exact_id, :user_comment, NOW(), NOW())'
    mysql.query_db(query,data)

    return redirect('/wall')

@app.route('/messages/<id>/delete')
def delete_message(id):

    query = 'DELETE FROM messages WHERE id = :id'
    data = {'id':id}
    mysql.query_db(query,data)

    return redirect('/wall')

@app.route('/comments/<id>/delete')
def delete_comment(id):

    query = 'DELETE FROM comments WHERE id = :id'
    data = {'id':id}
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')

app.run(debug=True)
