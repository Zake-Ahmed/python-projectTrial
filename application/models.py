from application import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30))
    firstName = db.Column(db.String(30),nullable = True)
    lastName = db.Column(db.String(30),nullable = True)
    post=db.relationship('Posts', backref='post')



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message= db.Column(db.String(280))
    likes = db.Column(db.Integer, default=0)
    userID = db.Column(db.Integer , db.ForeignKey(Users.id), nullable=False)
 