from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
API = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route('/')
def home():
    posts = requests.get(API).json()
    return render_template("index.html",posts = posts)

@app.route("/<id>")
def post_read(id):
    posts = requests.get(API).json()
    post_title = ""
    post_subtitle=""
    post_body =""
    for post in posts:
        if post["id"] == int(id):
            post_title = post["title"]
            post_subtitle =  post["subtitle"]
            post_body = post["body"]
            # po = Post(id,)
    return render_template("post.html",title = post_title,subtitle =post_subtitle, body =post_body)

if __name__ == "__main__":
    app.run(debug=True)
