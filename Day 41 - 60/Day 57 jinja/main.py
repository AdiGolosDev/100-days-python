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

# @app.route("/guess/<string:name>")
# def guess(name):
#     response_gender = requests.get("https://api.genderize.io", params={"name": name}).json()['gender']
#     response_age = requests.get("https://api.agify.io", params={"name": name}).json()['age']

#     return render_template("guess.html", age=response_age, gender=response_gender)

# too lazy to put this in an actual json file
all_posts = [
  {
    "id": 0,
    "title": "Day in the life of a fellow Klokan",
    "subtitle": "How a friendly neibourhood Klokan operates and his daily tasks",
    "body": "Klokan usually wakes up at unpredictable times of the day. He invests time into activities most fullfilling to him at the moment and doesn't pay attention to things like 'what other people think'. He loves his guitar, parents, video games, coding, writing, and messing around by writing random json formatted blogposts instead of actually coding the important stuff that Angela says in her 100-days-python course. He enjoys these activities as he doesn't mind time wasting, except when it occurs to him that he is indeed wasting time, like it is coming to him right now..."
  },
  {
    "id": 1,
    "title": "Klokan vs. the guitar he swore he'd practice today",
    "subtitle": "A tale of good intentions and three chords",
    "body": "Klokan picked up the guitar this morning with a real plan: scales, a bit of theory, maybe finally nail that chord transition he's been butchering for weeks. Forty minutes later he was just playing the same riff he already knows because it sounds cool and makes him feel like he's in a band that doesn't exist. Progress is a myth invented by people who finish their to-do lists. Klokan is not one of those people, and honestly he's made peace with it, mostly."
  },
  {
    "id": 2,
    "title": "The 100 Days of Python course strikes again",
    "subtitle": "Angela says do the exercise. Klokan says maybe later",
    "body": "Somewhere around day 14 Klokan opened the course, read the exercise prompt, understood it perfectly, and then closed the laptop to go write a json file about kangaroos instead. This is not procrastination, Klokan tells himself, this is 'creative cross-training'. Angela would probably disagree. Angela is usually right about these things, which is exactly why Klokan avoids checking in with Angela too often."
  },
  {
    "id": 3,
    "title": "Video games as a legitimate life choice",
    "subtitle": "Klokan defends his afternoon",
    "body": "Klokan sat down for 'just one match' and emerged three hours later, blinking at the sunlight like a creature freshly evolved. He doesn't regret it, not really, though there's a small nagging voice reminding him about the unfinished code and the guitar in the corner judging him silently. Klokan has learned to negotiate with that voice. Today the voice lost. Tomorrow is a new round of negotiations."
  },
  {
    "id": 4,
    "title": "Calling the parents, eventually",
    "subtitle": "Klokan means to call them every single day",
    "body": "Klokan thinks about calling his parents around lunchtime, then again in the evening, then somewhere close to midnight he actually does it, and it's always a good call, always worth it, always makes him wonder why he waited so long to just pick up the phone. He tells himself next time he'll call earlier. Klokan has told himself this before. Klokan is optimistic anyway."
  }
]

@app.route("/blog/<num>")
def get_blog(num):
    # blog_url = "https://www.npoint.io/docs/853efa5c4628642962ce"
    # response = requests.get(blog_url)
    # print(response.json())
    # all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
