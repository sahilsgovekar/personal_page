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
    content = db.Column(db.String(100000000))


@app.route("/sahil-govekar")
def home():
    return render_template("index.html")

@app.route("/")
def hom():
    return redirect(url_for("home"))

@app.route("/blog")
def blog():
    return render_template("blog.html")


# #rendering blog based on title
# @app.route("/blog/<int:index>")
# def show_post(index):5


if __name__ == "__main__":
    app.run(debug=True)
