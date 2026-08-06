from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()


# def delay_decorator(function):
#     def wrapper():
#         time.sleep(1)
#         function()
#     return wrapper

# @delay_decorator # wraps hi() in delay_decorator
# def hi():
#     print("Hi")

# def bye(): # not wrapped by delay_decorator
#     print("Bye")

# hi()
# bye()
# hi()