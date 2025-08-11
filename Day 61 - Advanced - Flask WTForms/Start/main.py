from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("CSRF_SECRET_KEY")
bootstrap = Bootstrap5(app)


# def my_length_check(form, field):
#     if len(field.data) > 50:
#         raise ValidationError('Field must be less than 50 characters')
#     elif len(field.data) < 8:
#         raise ValidationError('Field must be more than 5 characters')


class MyForm(FlaskForm):
    email = EmailField(
        label="email",
        validators=[
            Email(message="Please enter a valid email"),
            DataRequired(),
            Length(min=8, max=50, message="Email must be between 8 and 50 characters")
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            DataRequired(),
            Length(min=8, max=50, message="Password must be between 8 and 50 characters")
        ]
    )
    
    submit = SubmitField('Log In')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
