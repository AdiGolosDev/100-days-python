from flask import Flask, render_template, request
import json
import smtplib
import csv

with open("posts.json", "r", encoding="utf-8") as f:
    all_posts = json.load(f)

with open("email.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        MY_EMAIL = row["email"]
        MY_PASSWORD = row["pass"]
        TO_EMAIL = row["to"]

def send_email(name, email, phone, msg):
    to_send = f"Subject: {name.title()} has attempted to contact you!!\n\nTheir message: {msg} \nTheir email: {email} \nTheir phone: {phone}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=to_send)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_email(request.form["name"], request.form["email"], request.form["phone"], request.form["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

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
