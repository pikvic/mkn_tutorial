from flask import Flask, render_template
from random import choice

names = [
    'Alex',
    'Pete',
    'Arcady',
    'Kate'
]

counter = 0

app = Flask("app")

@app.get("/")
def index():
    сообщение = f"Hello, {choice(names)}"
    global counter
    counter += 1
    color = choice(["red", "blue", "green", "purple", "orange", "pink"])
    return render_template('index.html', message=сообщение, color=color, counter=counter)