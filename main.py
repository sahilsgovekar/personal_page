from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#table creation
class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    category = db.Column(db.String(50))
    content = db.Column(db.Text)


@app.route("/sahil-govekar")
def home():
    posts = db.session.query(Blog).all()
    return render_template("index.html", posts=posts)

@app.route("/")
def hom():
    return redirect(url_for("home"))

@app.route("/blog")
def blog():
    posts = db.session.query(Blog).all()
    return render_template("blog.html", posts=posts)


# #rendering blog based on title
@app.route("/blog/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(Blog).all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
