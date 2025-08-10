from flask import Flask
import time

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<e>{function()}</e>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/") # this is a decorator that tells Flask what URL should trigger the function below
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>'\
        '<p>This is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/3o7aD2saq1j0k4d5iY/giphy.gif" width=300>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

# Get hold of what a user enters in the URL
@app.route("/username/<name>") # <name> is a variable part of the URL that will be passed to the function as an argument
def greet(name):
    return f"Hello {name}"

@app.route("/username/<name>/<int:number>") # <name> is a variable part of the URL that will be passed to the function as an argument
def greetings(name, number):
    return f"Hello {name}, you are {number} years old!"

## Advanced Python decorator fxns
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            return wrapper 

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This blog post is created by {user.name}")


new_user = User("John")
new_user.is_logged_in = True
create_blog_post(new_user)  # This will print "This blog post is created by John"

# one other way people run flask apps
if __name__ == "__main__":
    app.run(debug=True) # runs the app on a local development server. Same as flask run command

