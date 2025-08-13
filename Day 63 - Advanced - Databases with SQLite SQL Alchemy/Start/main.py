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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



app = Flask(__name__)

# Create Database
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "/Day 63 - Advanced - Databases with SQLite SQL Alchemy/Start/books.db"
# Create extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# Create the table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Optional to allow each book object to be identified by its title, author, and rating when printed.
    def __repr__(self):
        return f"<Book {self.title} by {self.author} with rating{self.rating}>"


# Create the table schema inteh database. Requires application context.
with app.app_context():
    db.create_all()


class BookForm(FlaskForm):
    title = StringField("Title of Book", validators=[DataRequired()])
    author = StringField("Author of Book", validators=[DataRequired()])
    rating = SelectField("Book Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
    add = SubmitField("Add Book")


@app.route('/')
def home():
    ## Read all records of books from the database
    # Construct a quesry to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()  # Get all the books from the result
    # Render the index.html template with the list of books
    return render_template("index.html", books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # form = BookForm()
    # if form.validate_on_submit():
    #     new_book = {
    #         "title": form.title.data,
    #         "author": form.author.data,
    #         "rating": form.rating.data
    #     }
    #     all_books.append(new_book)
    #     return redirect(url_for('home'))
    if request.method == "POST":
        # Create a new book instance from the form data
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # Edit the record
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get("id")
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit-rating.html", book=book_selected)


@app.route("/delete")
def delete():
    # Delete the entry selected
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

