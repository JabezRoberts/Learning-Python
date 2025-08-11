from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def get_data():
    name = request.form.get('name') # this is a safer way to get form data and handles when the key is not found or data is missing
    # name = request.form['name'] # this will raise an error if the key is not found
    password = request.form.get('password')
    # password = request.form['password']
    return render_template('login.html', name=name, password=password)

# @app.get('/login')
# def login_get():
#     return "get the login page"

# @app.post('/login')
# def login_post():
#     return "post the login page"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
