from flask import Flask, request, render_template
import random

app = Flask("app")

posts = [
    {
        "user": "Pete",
        "title": "Warning!",
        "content": "Lorem ipsum hello world!",
        "date": "29-02-1988"
    }, 
    {
        "user": "Alex",
        "title": "Caution!",
        "content": "Text 2 is ipsum hello world!",
        "date": "38-02-1988"
    },
    {
        "user": "Mary",
        "title": "Hey!",
        "content": "Go here!",
        "date": "38-02-1988"
    }
]

@app.get("/")
def index():
    return render_template("index.html", posts=posts)

@app.get("/hello")
def hello():
    name = request.args.get("name", "John")
    return f"Hello, {name}!"