from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", random_number=random_number, year=year)


@app.route('/guess/<string:name>')
def guess(name):
    name = requests.get("https://api.genderize.io?name=" +name).json()["name"]
    gender = requests.get("https://api.genderize.io?name=" +name).json()["gender"]
    age = requests.get("https://api.agify.io?name=" +name).json()["age"]
    return render_template("guess.html", name=name, age=age,gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

