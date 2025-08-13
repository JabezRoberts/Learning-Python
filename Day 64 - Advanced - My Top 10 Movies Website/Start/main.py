from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)

IMDB_API_READ_ACCESS_TOKEN = os.getenv("API_Read_Access_Token")
IMDB_API_KEY = os.getenv("API_Key")

MOVIE_DB_SEARCH_URL="https://api.themoviedb.org/3/search/movie"
GET_MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/{movie_id}"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# params = {
#     "api_key": IMDB_API_KEY,
#     "query": movie_title
# }



headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNjUyMzBiZGE2ZTZiMzkzMTM1MzYwZDFkN2ZjZTNlMyIsIm5iZiI6MTY1NTE0MzcwNC42MjksInN1YiI6IjYyYTc3ZDE4N2UxMmYwMGUyODMxZDk4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c40DHQlFoiAjghh04ERpVHkIP5PildWpc2Ym0cjKMRg"
}

# CREATE DB
class Base(DeclarativeBase):
    pass

# CREATE TABLE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# Create extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)


# Create the table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False) 
    description: Mapped[str] = mapped_column(String(500), nullable=False) 
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(2500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(1000), nullable=False)
    
    # Optional to allow each movie object to be identified by its title, year, and rating when printed.
    def __repr__(self):
        return f"<Movie {self.title} from the year {self.year} with rating {self.rating} and ranking {self.ranking}>"


# Create the table schema in the database
with app.app_context():
    db.create_all()
    

# Create the table schema in the database. Requires application context
class MovieForm(FlaskForm): 
    rating = StringField("Your rating out of 10. Eg. 6.5", validators=[DataRequired()])
    review = StringField("Add Your Review", validators=[DataRequired()])
    update = SubmitField("Update")

# Form to find a movie to add to the database
class FindMovieForm(FlaskForm):
    title = StringField("Enter the movie title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

new_movie = Movie(    
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)


# Create Record
with app.app_context():
    db.session.add(new_movie)  # Add the new movie to the session
    db.session.add(second_movie)  # Add the second movie to the session
    db.session.commit()  # Commit the session to save the changes


@app.route("/")
def home():
    # Read all records of movies from tehe database 
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars().all() # Get all the movies from the result
    # Render the index.html template with the list of movies
    
    # now we rank the movies based on their ratings
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies = all_movies)


@app.route("/edit", methods=["Get", "POST"])
def edit():
    form = MovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, id=movie_id)
    
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form = form)
    
    # if request.method == "POST":
    #     # Get the movie ID from the form data
    #     movie_id = request.form["id"]
    #     movie_to_update = db.get_or_404(Movie, id=movie_id)
        
    #     # Update the movie's rating with the new value the uer entered in the form
    #     movie_to_update.rating = request.form["rating"]
    #     db.session.commit()
    # movie_id = request.args.get("id")
    # movie_selected = db.get_or_404(Movie, id=movie_id)
    
    # # Tutor's solution
    # form = MovieForm()
    # movie_id = request.args.get("id")
    # movie = db.get_or_404(Movie, movie_id)
    # if form.validate_on_submit():
    #     movie.rating = float(form.rating.data)
    #     movie.review = form.review.data
    #     db.session.commit()
    #     return redirect(url_for('home'))
    # return render_template("edit.html", movie=movie, form=form)
    
    return render_template("edit.html", movie=movie_selected)


# Delete Record
@app.route("/delete")
def delete():
    # Delete movie from the database
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, id=movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


# Add a movie
@app.route("/add", methods=["GET", "POST"])
def add():
    # if request.method == "POST":
    #     # Create a new movie instance from the form data
    #     new_movie = Movie(
    #         title = request.form["title"],
    #         year = request.form["year"],
    #         description = request.form["description"],
    #         rating = request.form["rating"],
    #         ranking = request.form["ranking"],
    #         review = request.form["review"],
    #         img_url = request.form["img_url"],
    #     )
        
        # Add the new movie to the session and commit the changes
        # db.session.add(new_movie)
        # db.session.commit()
        # return redirect(url_for('home'))
    
    
    form = FindMovieForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": IMDB_API_KEY,
            "query": movie_title
        })
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)
    # return render_template("add.html")


# Find a movie from the IMDB database via API
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{GET_MOVIE_DETAILS_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience 
        #e.g. Hindi speakers then you might choose "hi-IN"
        
        response = requests.get(movie_api_url, params={
            "api_key": IMDB_API_KEY,
            "language": "en-US"
        })
        data = response.json()
        new_movie = Movie(
            title = data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year = data["release_date"].split("-")[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data["overview"],
        )
        
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
