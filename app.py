from flask import Flask, request, render_template, redirect
from pathlib import Path
import datetime

app = Flask("app")

POSTS_DIR = Path('posts')

def create_post(post):
    with open(POSTS_DIR / f'post{post["id"]}.txt', 'wt') as f:
        f.write(str(post["id"]) + '\n')
        f.write(post["user"] + '\n')
        f.write(post["title"] + '\n')
        f.write(str(post["date"]) + '\n')
        f.write(post["content"])

def get_posts():
    posts = []
    for file in POSTS_DIR.iterdir():
        with open(file, 'rt') as f:
            lines = f.read().split('\n')
            print(lines)
        post = {
            "id": lines[0],
            "user": lines[1],
            "title": lines[2],
            "date": lines[3],
            "content": lines[4]
        }
        posts.append(post)
    return posts

@app.get("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.get("/add_post")
def add_post():
    return render_template("add_post.html")

@app.post("/add_post")
def append_post():
    post_id = len(get_posts()) + 1
    user = request.form["user"]
    title = request.form["title"]
    content = request.form["content"]
    date = datetime.date.today()
    create_post({"id": post_id, "user": user, "title": title, "content": content, "date": date})
    return redirect("/")