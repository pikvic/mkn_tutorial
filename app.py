from flask import Flask, request, render_template
from pathlib import Path

app = Flask("app")

POSTS_FILE = Path('posts.txt')

print(POSTS_FILE.absolute())

if not POSTS_FILE.exists():
    with open(POSTS_FILE, 'wt') as f:
        pass

def get_posts():
    posts = []
    post_id = 1
    post = get_post(post_id)
    while post:
        posts.append(post)
        post_id += 1
        post = get_post(post_id)
    return posts

def get_post(post_id):
    with open(POSTS_FILE, 'rt') as f:
        # skip posts before post_id
        for i in range(post_id - 1):
            for i in range(5):
                data = f.readline()
            if not data:
                print(data)
                return None
        post_id = f.readline()
        if not post_id:
            print(post_id)
            return None
        user = f.readline()
        title = f.readline()
        content = f.readline()
        date = f.readline()
        post = {"id": post_id, "user": user, "title": title, "content": content, "date": date}
        return post

def create_post(post):
    with open(POSTS_FILE, 'a') as f:
        for value in post.values():
            f.write(str(value))
            f.write('\n')

def delete_post(post_id):
    pass


    # {
    #     "id": 1,
    #     "user": "Pete",
    #     "title": "Warning!",
    #     "content": "Lorem ipsum hello world!",
    #     "date": "29-02-1988"
    # }, 
print(get_posts())

@app.get("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.get("/hello")
def hello():
    name = request.args.get("name", "John")
    return f"Hello, {name}!"