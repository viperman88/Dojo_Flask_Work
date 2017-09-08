from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    allNinjas = True
    return render_template('ninjas.html', allNinjas=allNinjas)

@app.route('/ninja/<color>')
def getColor(color):
    allNinjas = False
    return render_template('ninjas.html', color=color, allNinjas=allNinjas)

app.run(debug=True)
