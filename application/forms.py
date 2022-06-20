from xml.etree.ElementTree import SubElement
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired,Length

class TaskForm(FlaskForm):
    task_name = StringField("Task")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    userName= StringField("User Name")
    firstName = StringField("First Name")
    lastName = StringField("Last Name")
    submit= SubmitField("Submit")

class PostForm(FlaskForm):
    user = SelectField("user" ,choices=[])
    message = StringField("message", validators=[DataRequired(),Length(max=280)])
    submit= SubmitField("Submit")
