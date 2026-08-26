from flask import Flask, render_template, request, redirect, url_for
import json
import os

if os.path.exists("books.json") and os.path.getsize("books.json") > 0:
    with open("books.json", "r") as f:
        all_books = json.load(f)
else:
    all_books = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "name": request.form["name"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)

        with open("books.json", "w") as f:
            json.dump(all_books, f, indent=2)

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
