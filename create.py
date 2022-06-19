from application import db
from application.models import ToDo,Users,Posts

db.drop_all()
db.create_all()
sample_todo = ToDo(
    task_name = "Test ToDo",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()
rootUser = Users(userName="root",firstName="root",lastName="root")
db.session.add(rootUser)
db.session.commit()
rootUser = Users(userName="admin",firstName="root",lastName="root")
db.session.add(rootUser)
db.session.commit()
rootPost= Posts(message="root" ,userID=1)

db.session.add(rootPost)
db.session.commit()
rootPost= Posts(message="admin" ,userID=2)

db.session.add(rootPost)
db.session.commit()
