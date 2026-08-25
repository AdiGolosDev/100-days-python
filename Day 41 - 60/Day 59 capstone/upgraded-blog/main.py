from flask import Flask, render_template
import json

with open("posts.json", "r", encoding="utf-8") as f:
    all_posts = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:pid>')
def post(pid):
    requested_post = None
    for p in all_posts:
        if p["id"] == pid:
            requested_post = p
            break
    return render_template('post.html', post=requested_post)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
