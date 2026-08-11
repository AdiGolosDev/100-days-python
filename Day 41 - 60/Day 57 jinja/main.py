from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, yr=current_year)

@app.route("/guess/<string:name>")
def guess(name):
    response_gender = requests.get("https://api.genderize.io", params={"name": name}).json()['gender']

    response_age = requests.get("https://api.agify.io", params={"name": name}).json()['age']

    return render_template("guess.html", age=response_age, gender=response_gender)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
