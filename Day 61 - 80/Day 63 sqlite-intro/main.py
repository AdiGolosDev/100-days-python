from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# --- sqlite3 setup ---
db = sqlite3.connect("books.db", check_same_thread=False)
db.row_factory = sqlite3.Row  # lets us access columns by name, e.g. row["title"]
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL UNIQUE,
        author VARCHAR(250) NOT NULL,
        rating FLOAT NOT NULL
    )
""")
db.commit()

# if os.path.exists("books.json") and os.path.getsize("books.json") > 0:
#     with open("books.json", "r") as f:
#         all_books = json.load(f)
# else:
#     all_books = []

# --- SQLAlchemy setup --- I think its overkill for a simple book website
# class Base(DeclarativeBase):
#     pass
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# db = SQLAlchemy(app, model_class=Base)
#
# class Book(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
#     author: Mapped[str] = mapped_column(String(250), nullable=False)
#     rating: Mapped[float] = mapped_column(Float, nullable=False)
#
# with app.app_context():
#     db.create_all()

app = Flask(__name__)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        cursor.execute(
            "INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
            (request.form["name"], request.form["author"], request.form["rating"])
        )
        db.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)