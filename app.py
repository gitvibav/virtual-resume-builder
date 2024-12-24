from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class ResumeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    portfolio = StringField('Portfolio URL')
    education = StringField('Education', validators=[DataRequired()])
    education_from = StringField('Education From Year')
    education_to = StringField('Education To Year')
    course_taken = StringField('Course Taken')
    gpa = StringField('GPA')
    languages = StringField('Languages', validators=[DataRequired()])
    libraries = StringField('Libraries/Frameworks', validators=[DataRequired()])
    tools = StringField('Tools', validators=[DataRequired()])
    others = StringField('Others', validators=[DataRequired()])
    submit = SubmitField('Generate Resume')

@app.route("/", methods=["GET", "POST"])
def index():
    form = ResumeForm()

    data = {
        "name": "",
        "email": "",
        "phone": "",
        "portfolio": "",
        "education": "",
        "education_from": "",
        "education_to": "",
        "course_taken": "",
        "gpa": "",
        "projects": [],
        "experience": [],
        "skills": {
            "languages": "",
            "libraries": "",
            "tools": "",
            "others": "",
        }
    }

    if request.method == "POST":
       
        data = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "phone": request.form.get("phone", "").strip(),
            "portfolio": request.form.get("portfolio", "").strip(),
            "education": request.form.get("education", "").strip(),
            "education_from": request.form.get("education_from", "").strip(),
            "education_to": request.form.get("education_to", "").strip(),
            "course_taken": request.form.get("course_taken", "").strip(),
            "gpa": request.form.get("gpa", "").strip(),
            "projects": [
                {
                    "title": request.form.getlist("projects[]")[i].strip(),
                    "description": request.form.getlist("project_details[]")[i].strip(),
                }
                for i in range(len(request.form.getlist("projects[]")))
            ],
            "experience": [
                {
                    "title": request.form.getlist("experience_positions[]")[i].strip(),
                    "from_year": request.form.getlist("experience_from[]")[i].strip(),
                    "to_year": request.form.getlist("experience_to[]")[i].strip(),
                    "description": request.form.getlist("experience_details[]")[i].strip(),
                }
                for i in range(len(request.form.getlist("experience_positions[]")))
            ],
            "skills": {
                "languages": request.form.get("languages", "").strip(),
                "libraries": request.form.get("libraries", "").strip(),
                "tools": request.form.get("tools", "").strip(),
                "others": request.form.get("others", "").strip(),
            }
        }
        return render_template("preview.html", data=data)

    return render_template("index.html", form=form, data=data)

if __name__ == "__main__":
    app.run(debug=True)