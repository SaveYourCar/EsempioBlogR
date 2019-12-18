from datetime import datetime

from flask import session

from core.config import db
from core.models.postsModel import Post

# funzione che estrae tutti i post dal db
def get_posts():
    posts = Post.query.all()
    return posts

# funzione che estrae tutti i post dal db relativi ad uno specifico utente
def get_posts_by_user():
    posts = Post.query.filter_by(user_id=session['user_id'])
    return posts

# funzione che estrae il post che ha come id quello in ingresso all funzione, il .first() serve per dirgli di prendere il primo
def get_post(sno):
    post = Post.query.filter_by(sno=sno).first()
    return post

def get_post_for_slug(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return post

# funzione che permette di inserire un post nel db
def insert_post(form):
    # id dell'utente loggato recuperato dalla sessione
    user_id = session['user_id']

    #parametri raccolti dal form html relativo ai post
    box_title = form.get('title')
    tline = form.get('tline')
    slug = form.get('slug')
    content = form.get('content')
    img_file = form.get('img_file')
    date = datetime.now()

    # istanzio un oggetto post con tutte le informazioni e poi lo inserisco nel db
    post = Post(user_id=user_id, title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
    db.session.add(post)
    db.session.commit()

# funzione che peremtte di modificare un post gia creato.
# Comportamento simile alla funzione insert_post() ma in questo caso
# devo prima estrarre il post dal db per poterlo poi modificare
def update_post(form, sno):

    # parametri recuperati dal form
    box_title = form.get('title')
    tline = form.get('tline')
    slug = form.get('slug')
    content = form.get('content')
    img_file = form.get('img_file')
    date = datetime.now()

    # estraggo il post da modificare
    post = Post.query.filter_by(sno=sno).first()
    # attribuisco i nuovi valori ai vari campi e poi salvo sul db
    post.title = box_title
    post.slug = slug
    post.content = content
    post.tagline = tline
    post.img_file = img_file
    post.date = date
    db.session.commit()

# funzione che permette di cancellare un post attraverso il suo id
def delete_post(sno):
    post = Post.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()

