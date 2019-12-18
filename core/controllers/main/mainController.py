"""
in questo controller sono stati gestiti tutti gli handler relativi alla sezione principale del blog.

"""

import math

from flask import Blueprint, render_template, request

from core.config import configuration_params as params, mail
from core.data_access.contactsDA import insert_contact
from core.data_access.postsDA import get_post_for_slug, get_posts

main = Blueprint("main", __name__)


# home page del blog, estraggo tutti i post e creo una paginazione in modo da non vederli tutti assieme ma divisi per gruppi
@main.route("/")
def home():
    posts = get_posts()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    #[0: params['no_of_posts']]
    #posts = posts[]
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page= int(page)
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    #Pagination Logic
    #First
    if (page==1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template("index.html", params=params, posts=posts, prev=prev, next=next)


@main.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = get_post_for_slug(post_slug)
    return render_template('post.html', params=params, post=post)


@main.route("/about")
def about():
    return render_template('about.html', params=params)



@main.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        insert_contact(request.form)
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + phone
                          )
    return render_template('contact.html', params=params)