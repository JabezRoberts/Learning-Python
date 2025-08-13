from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# create the Flask app
app = Flask(__name__)


# First create the db object using the SQLAlchemy constructor.

# Pass a subclass of either DeclarativeBase or DeclarativeBaseNoMeta to the constructor.
class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
# Create an SQLite database called new-books-collection.db. Remember to initialise the app.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


# Create the extension
# Create the SQLAlchemy object with the base class
# This object will be used to interact with the database.
db = SQLAlchemy(model_class=Base)


# initialize the app with the extension
db.init_app(app)


## CREATE TABLE
# Define the model
# Subclass db.Model to define a model class. The model will generate a table name by converting the CamelCase class name to snake_case.
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True) # Primary key field
    # Define the other fields with their types and constraints
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Unique and not null
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title} by {self.author} with rating {self.rating}>'



# Create table schema in the database. Requires application context.
# Create the table in the database
# After all models and tables are defined, call SQLAlchemy.create_all() to create the table schema in the database. This requires an application context. Since you’re not in a request at this point, create one manually.

with app.app_context():
    db.create_all()


# Create Record
with app.app_context():
    new_book = Book(id=1, title="The Desire of Ages", author="Ellen G. White", rating=9.5)
    db.session.add(new_book)  # Add the new book to the session
    db.session.commit()  # Commit the session to save the changes