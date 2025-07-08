from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class ReportIssueForm(FlaskForm):
    title = StringField("Issue Title", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    image = FileField("Upload Image (optional)", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField("Submit Report")

class TrackIssueForm(FlaskForm):
    issue_id = StringField("Enter Issue ID", validators=[DataRequired()])
    submit = SubmitField("Track")
