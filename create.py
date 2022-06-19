from application import db
from application.models import ToDo

db.drop_all()
db.create_all()
sample_todo = ToDo(
    task_name = "Test ToDo",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()