from application import app

#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

#db = SQLAlchemy(app)

#class ToDo(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    task_name = db.Column(db.String(30))
#    completed = db.Column(db.Boolean, default=False)

#db.create_all()
#sample_todo = ToDo(
#    task_name = "Test ToDo",
#    completed = False
#)
#db.session.add(sample_todo)
#db.session.commit()

#@app.route('/')
#def index():
#    todo = ToDo.query.first()
#    return todo.task_name

#@app.route('/add')
#def add():
#    return 'Added a new ToDo'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)