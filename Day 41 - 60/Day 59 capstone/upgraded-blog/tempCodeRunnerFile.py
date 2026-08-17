@app.route('/post/<int:pid>')
def post(pid):
    requested_post = None
    for post in all_posts:
        if post["id"] == pid:
            requested_post = post
            break
    return render_template('post.html', id=requested_post)