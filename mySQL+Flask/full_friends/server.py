from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def users():

    query = 'SELECT * FROM users'
    users = mysql.query_db(query)

    return render_template('index.html', all_users = users)

@app.route('/friends', methods = ['POST'])
def create():

    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'
    data = {
        'first_name': request.form['firstName'],
        'last_name': request.form['lastName'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/edit', methods = ['POST'])
def edit(id):
    data = {
        'id': id
    }
    query = "SELECT * FROM users WHERE id = :id LIMIT 1"
    friend = mysql.query_db(query, data)

    return render_template("edit.html", person=friend)

@app.route('/friends/<id>', methods = ['POST'])
def update(id):

    data = {
        'id': id,
        'first_name': request.form['firstName'],
        'last_name': request.form['lastName'],
        'email': request.form['email']
    }
    query = ' UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id LIMIT 1'
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['POST'])
def delete(id):

    query = 'DELETE FROM users WHERE id = :id '
    data = {'id':id}
    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
