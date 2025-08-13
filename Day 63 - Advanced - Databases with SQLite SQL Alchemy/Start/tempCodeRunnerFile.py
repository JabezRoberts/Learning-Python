'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

all_books = []


class BookForm(FlaskForm):
    title = StringField("Title of Book", validators=[DataRequired()])
    author = StringField("Author of Book", validators=[DataRequired()])
    rating = SelectField("Book Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
    add = SubmitField("Add Book")


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add")
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = {
            "title": form.title.data,
            "author": form.author.data,
            "rating": form.rating.data
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)

