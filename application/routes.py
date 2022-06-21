from application import app, db
from application.models import ToDo,Users,Posts
from application.forms import TaskForm ,PostForm,UserForm
from flask import Flask, redirect, url_for, render_template, request


@app.route('/index')
def index():
    posts = Posts.query.all()
  

    # empstr = ""
    # for t_name in todo:
    #     empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    # return empstr
    return render_template("task.html", ToDo=posts)

@app.route('/indexU')
def indexU():
    posts = Users.query.all()
  

    # empstr = ""
    # for t_name in todo:
    #     empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    # return empstr
    return render_template("userList.html", ToDo=posts)

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/')
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

    if form.validate_on_submit():
        todo.message = form.message.data
            
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.message.data = todo.message
        return render_template('update.html', todo=todo,form=form)
    elif request.method == 'POST':
        todo.message = form.message.data
            
        db.session.commit()
        return redirect(url_for('index'))





@app.route('/delete/<id>')
def delete(id):
    task_del =Posts.query.get(id)
    db.session.delete(task_del)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/like/<id>')
def like(id):
    task_del = Posts.query.get(id)
    task_del.likes +=1
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/dislike/<id>')
def dislike(id):
    task_del = Posts.query.get(id)
    task_del.likes -=1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addUser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = Users(
                userName = form.userName.data,
                firstName = form.firstName.data,
                lastName = form.lastName.data
                
            )
            User=Users.query.all()
            for users in User:
                if users.userName==form.userName.data:
                    form1 = UserForm()
                    return render_template('addUser.html', form=form1 , error="User name already taken pick another one :)")

            
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addUser.html', form=form,error="")


@app.route('/user/<id>')
def user(id):
    posts = Posts.query.filter_by(userID=id)
    userName=Users.query.filter_by(id=id).first()
  

    # empstr = ""
    # for t_name in todo:
    #     empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    # return empstr
    return render_template("user.html", ToDo=posts,username=userName.userName,id=id)

@app.route('/deleteU/<id>')
def deleteU(id):
    task_del =Users.query.get(id)
    db.session.delete(task_del)
    db.session.commit()
    return redirect(url_for('indexU'))


@app.route('/updateU/<id>', methods=['GET', 'POST'])
def updateU(id):
    form = UserForm()
    todo = Users.query.get(id)
    User=Users.query.all()

    if form.validate_on_submit():
        todo.firstName = form.firstName.data
        todo.lastName = form.lastName.data

            
        db.session.commit()
        return redirect(url_for('indexU'))
    elif request.method == 'GET':
        form.firstName.data = todo.firstName 
        form.lastName.data = todo.lastName 
            
        return render_template('updateU.html', todo=todo,form=form)
    elif request.method == 'POST':
        todo.firstName = form.firstName.data
        todo.lastName = form.lastName.data
            
        db.session.commit()
        return redirect(url_for('indexU'))