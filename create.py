from application import db
from application.models import ToDo,Users,Posts

db.drop_all()
db.create_all()
sample_todo = ToDo(
    task_name = "Test ToDo",
    completed = False
)
rootUser = Users(userName="root",firstName="root",lastName="root")
rootPost= Posts(massage="root")

db.session.add(sample_todo)
db.session.commit()