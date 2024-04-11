from flask import render_template, request
from app import app
from app.tasks import add_task, subtract_task

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = add_task.delay(a, b)
    return f"The result of {a} + {b} is: {result.get()}"

@app.route('/subtract', methods=['POST'])
def subtract():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = subtract_task.delay(a, b)
    return f"The result of {a} - {b} is: {result.get()}"