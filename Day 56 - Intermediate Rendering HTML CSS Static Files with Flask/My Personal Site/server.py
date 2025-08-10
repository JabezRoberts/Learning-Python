from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/") # this is a decorator that tells Flask what URL should trigger the function below
def home():
    return render_template("jabez.html")


if __name__ == "__main__":
    app.run(debug=True)