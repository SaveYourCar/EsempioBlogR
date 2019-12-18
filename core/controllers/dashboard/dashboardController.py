import os

from flask import Blueprint, redirect, render_template, session, request
from werkzeug.utils import secure_filename

from core.config import configuration_params as params
from core.data_access.postsDA import get_posts, insert_post, update_post, get_post, delete_post

dashboard = Blueprint("dashboard", __name__)

@dashboard.before_request
def before_request_func():
    if ('user' in session and session['user'] == params['admin_user']):
        pass
    else:
        return render_template('login.html', params=params)


@dashboard.route("/dashboard", methods=['GET', 'POST'])
def dashboard_index():
    if 'user' in session:
        posts = get_posts()
        return render_template('dashboard.html', params=params, posts = posts)
"""
         and session['user'] == params['admin_user']):
        
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            posts = get_posts()
            return render_template('dashboard.html', params=params, posts = posts)

    return render_template('login.html', params=params)
"""

@dashboard.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit_post(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            if sno=='0':
                insert_post(request.form)
            else:
                update_post(request.form, sno)
                return redirect('/edit/'+sno)
        post = get_post(sno)
        return render_template('edit.html', params=params, post=post, sno=sno)


@dashboard.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(params['upload_location'], secure_filename(f.filename) ))
            return "Uploaded successfully"


@dashboard.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        delete_post(sno)
    return redirect('/dashboard')

