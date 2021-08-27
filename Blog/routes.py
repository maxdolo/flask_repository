from flask import render_template, redirect, url_for

from Blog import app, db
from Blog.models import Post
from Blog.forms import PostForm

@app.route("/")
def homepage():
    # posts = [
    #     {"titolo":"Primo Post", "body":"Questo è il mio Primo Post"},
    #     {"titolo":"Secondo Post", "body":"Questo è il mio Secondo Post"},

    # ]
    posts = Post.query.all()
    flag = True
    return render_template('homepage.html', posts=posts, flag=flag)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contatti")
def contatti(): 
    return render_template('contatti.html')

@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    form = PostForm(meta={'csrf': False})
    if form.validate_on_submit():
        new_post = Post(titolo=form.titolo.data, descrizione=form.descrizione.data,
                        body=form.body.data, user_id=1)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('create-post.html', form=form)