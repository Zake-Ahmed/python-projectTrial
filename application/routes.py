from application import app, db
from application.models import ToDo
from application.forms import TaskForm 
from flask import Flask, redirect, url_for, render_template, request


@app.route('/')
def index():
    todo = ToDo.query.all()
    # empstr = ""
    # for t_name in todo:
    #     empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    # return empstr
    return render_template("task.html", ToDo=todo)

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/home')
def home():
    return render_template("home.html")
# @app.route('/add/<t_name>')
# def add(t_name):
#     task = ToDo(task_name=t_name) 
#     db.session.add(task)
#     db.session.commit()
#     return "Added to ToDo List"

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = ToDo(
                task_name = form.task_name.data,
                completed = form.completed.data
            )
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addTask.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDo.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    todo = ToDo.query.get(id)
    todo.task_name = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<t_name>')
def delete(t_name):
    task_del = ToDo.query.filter_by(task_name=t_name).first()
    db.session.delete(task_del)
    db.session.commit()
    return redirect(url_for('index'))
