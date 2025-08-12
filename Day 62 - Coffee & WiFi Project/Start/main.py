from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    location = URLField("Locate Cage On Google Maps URL", validators=[DataRequired(),URL(message="Please enter a valid URL.")])
    open = StringField("Opening Time", validators=[DataRequired()])
    close = StringField("Closing Time", validators=[DataRequired()])
    cafe_rating = StringField("Rating", validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Speed", choices=["💥", "⚡", "⚡⚡", "⚡⚡⚡", "⚡⚡⚡⚡", "⚡⚡⚡⚡⚡"], validators=[DataRequired()])
    power_rating = SelectField("Power Outlet Availability", choices=["💥", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    form = CafeForm()
    if form.validate_on_submit():
        with open("Day 62 - Coffee & WiFi Project\Start\cafe-data.csv", mode="a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([])  # writes a blank line
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.cafe_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Day 62 - Coffee & WiFi Project\Start\cafe-data.csv', newline='', encoding='utf-8') as file:
        csv_data = csv.reader(file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
