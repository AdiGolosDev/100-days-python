from flask import Flask, render_template

all_posts = [] # need to actually add posts and figure out what format to do for this

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:pid>')
def post(pid):
    requested_post = None
    for post in all_posts:
        if post["id"] == pid:
            requested_post = post
            break
    return render_template('post.html', id=requested_post)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
