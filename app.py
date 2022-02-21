from flask import Flask, render_template
from random import choice

names = [
    'Alex',
    'Pete',
    'Arcady',
    'Kate'
]

app = Flask("app")

@app.get("/")
def index():
    сообщение = f"Hello, {choice(names)}"
    color = choice(["red", "blue", "white"])
    return render_template('index.html', message=сообщение, color=color)