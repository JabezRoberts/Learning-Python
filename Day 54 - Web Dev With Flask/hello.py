from flask import Flask
import time

app = Flask(__name__) # initialize a new Flask app only requires the import name

# A decorator is a function that modifies another function
# In this case, it modifies the function hello_world to be a route handler for the root URL
# Being able to treat functions as first-class objects is a powerful feature of Python where we can pass functions as arguments to other functions
@app.route("/") # this is a decorator that tells Flask what URL should trigger the function below
def hello_world():
    return "Hello, World!"

# one other way people run flask apps
if __name__ == "__main__":
    app.run() # runs the app on a local development server. Same as flask run command


## Python decorator fxn
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before the function call
        function()
        function()
        # Do something after the function call
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")


def say_goodbye():
    print("Goodbye!")
    

@delay_decorator
def say_hello_decorated():
    delayed_hello = delay_decorator(say_hello)
    delayed_hello()  # This will print "Hello!" after a 2-second delay
def say_goodbye_decorated():
    delayed_goodbye = delay_decorator(say_goodbye)
    delayed_goodbye()  # This will print "Goodbye!" after a 2-second delay


def say_greeting():
    print("How are ya?")

# @delay_decorator is called syntactic sugar for say_greeting = delay_decorator(say_greeting)
decorated_function = delay_decorator(say_greeting)
decorated_function()  # This will print "How are ya?" after a 2-second delay