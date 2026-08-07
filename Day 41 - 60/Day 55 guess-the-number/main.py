from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center;">Guess a number from 1 - 10</h1>' \
    '<p style="text-align: center;">To guess the number type in /your-guess into the url</p>' \
    '<div style="text-align: center;">' \
    '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnd5eWR4cmgwMm9pbmFqZ3ZvaW5ocXZwMjJja2V2bnlwazF6cjVyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iixdMr6cSURW/giphy.gif" width=500>' \
    '</div>'

@app.route("/<int:number>")
def guess(number):
    n = random.randint(1,10)
    if number == n:
        return '<h1 style="text-align: center;"> YOU GUESSED RIGHT!!!</h1>' \
        '<div style="text-align: center;">' \
        '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWtvY2tqaHVkemVzbTRwdmMwdWxxbTRzYXAxdDE1bjF4anlwdjkxaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C3brYLms1bhv2/giphy.gif" width=500>' \
        '</div>'
    else: 
        return '<h1 style="text-align: center;"> You guessed wrong... </h1>' \
        '<div style="text-align: center;">' \
        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmh5ajF4MTJyYXdkYm9reTFya2Eyb2RlbjY1N3ZxZnV3dHpzdzc2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OSwxaHg7OpHRFVIobJ/giphy.gif" width=500>' \
        '</div>'

if __name__ == "__main__":
    app.run(debug=True)
