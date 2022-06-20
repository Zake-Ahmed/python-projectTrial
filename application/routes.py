from application import app, db
from application.models import ToDo,Users,Posts
from application.forms import TaskForm ,PostForm,UserForm
from flask import Flask, redirect, url_for, render_template, request


@app.route('/')
def index():
    posts = Posts.query.all()
  

    # empstr = ""
    # for t_name in todo:
    #     empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    # return empstr
    return render_template("task.html", ToDo=posts)

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
    form = PostForm()
    form.user.choices=[(users.id,users.userName) for users in Users.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = Posts(
                message = form.message.data,
                userID = form.user.data
                
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

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = PostForm()
    todo = Posts.query.get(id)
    if request.method == 'POST':
        todo.message = form.message.data
            
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', todo=todo,form=form)


@app.route('/delete/<t_name>')
def delete(t_name):
    task_del = Posts.query.filter_by(message=t_name).first()
    db.session.delete(task_del)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/like/<id>')
def like(id):
    task_del = Posts.query.get(id)
    task_del.likes +=1
    db.session.commit()
    return redirect(url_for('index'))