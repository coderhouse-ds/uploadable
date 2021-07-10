import json
import math
from datetime import date

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


with open('config.json','r') as c:
    params = json.load(c)["params"]
local_server=True
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Posts(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    category = db.Column(db.String(15),nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(200),nullable=False)
    date = date.today().strftime("%d/%m/%y")
    code1_title = db.Column(db.String(70),nullable=False)
    code1 = db.Column(db.String(100000),nullable=False)
    code2_title = db.Column(db.String(70), nullable=True)
    code2 = db.Column(db.String(100000), nullable=True)
    code3_title = db.Column(db.String(70), nullable=True)
    code3 = db.Column(db.String(100000), nullable=True)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/fullcode/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    print(post)
    return render_template('fullcode.html', params=params, post=post)


@app.route("/webdevelopment/lt/showinfo",methods=['GET'])
def webdevelopmentlt():
    posts = Posts.query.filter(Posts.category=='webdevlopmentlt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    # [0:params['no_of_posts']]
    # PAGINATION Logic
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/webdevelopment/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/webdevelopment/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/webdevelopment/lt/showinfo?page=" + str(page - 1)
        next = "/webdevelopment/lt/showinfo?page=" + str(page + 1)

    # print(posts)
    return render_template('showinfo.html', params=params, posts=posts,prev=prev,next=next)
@app.route("/webdevelopment/pr/showinfo",methods=['GET'])
def webdevelopmentpr():
    posts = Posts.query.filter(Posts.category=='webdevlopmetpr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/webdevelopment/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/webdevelopment/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/webdevelopment/pr/showinfo?page=" + str(page - 1)
        next = "/webdevelopment/pr/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/python/lt/showinfo",methods=['GET'])
def pythonlt():
    posts = Posts.query.filter(Posts.category=='pythonlt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/python/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/python/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/python/lt/showinfo?page=" + str(page - 1)
        next = "/python/lt/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/python/pr/showinfo",methods=['GET'])
def pythonpr():
    posts = Posts.query.filter(Posts.category=='pythonpr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/python/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/python/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/python/pr/showinfo?page=" + str(page - 1)
        next = "/python/pr/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/tkinter/lt/showinfo",methods=['GET'])
def tkinterlt():
    posts = Posts.query.filter(Posts.category=='tkinterlt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/tkinter/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/tkinter/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/tkinter/lt/showinfo?page=" + str(page - 1)
        next = "/tkinter/lt/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/tkinter/pr/showinfo",methods=['GET'])
def tkinterpr():
    posts = Posts.query.filter(Posts.category=='tkinterpr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/tkinter/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/tkinter/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/tkinter/pr/showinfo?page=" + str(page - 1)
        next = "/tkinter/pr/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/javacore/lt/showinfo",methods=['GET'])
def javacorelt():
    posts = Posts.query.filter(Posts.category=='javacorelt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/javacore/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/javacore/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/javacore/lt/showinfo?page=" + str(page - 1)
        next = "/javacore/lt/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/javacore/pr/showinfo",methods=['GET'])
def javacorepr():
    posts = Posts.query.filter(Posts.category=='javacorepr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/javacore/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/javacore/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/javacore/pr/showinfo?page=" + str(page - 1)
        next = "/javacore/pr/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/c/lt/showinfo",methods=['GET'])
def clt():
    posts = Posts.query.filter(Posts.category=='clt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/c/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/c/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/c/lt/showinfo?page=" + str(page - 1)
        next = "/c/lt/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/c/pr/showinfo",methods=['GET'])
def cpr():
    posts = Posts.query.filter(Posts.category=='cpr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/c/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/c/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/c/pr/showinfo?page=" + str(page - 1)
        next = "/c/pr/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/javascript/lt/showinfo",methods=['GET'])
def javascriptlt():
    posts = Posts.query.filter(Posts.category=='javascriptlt').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/javascript/lt/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/javascript/lt/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/javascript/lt/showinfo?page=" + str(page - 1)
        next = "/javascript/lt/showinfo?page=" + str(page + 1)

    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/javascript/pr/showinfo",methods=['GET'])
def javascriptpr():
    posts = Posts.query.filter(Posts.category=='javascriptpr').all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    # [0:params['no_of_posts']]
    # PAGINATION Logic
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = '#'
        next = "/javascript/pr/showinfo?page=" + str(page + 1)
    elif (page == last):
        prev = "/javascript/pr/showinfo?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/javascript/pr/showinfo?page=" + str(page - 1)
        next = "/javascript/pr/showinfo?page=" + str(page + 1)

    # print(posts)
    return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)

app.run(debug=True)

# @app.route("/showinfo",methods=['GET'])
# def showinfo():
#     # posts = Posts.query.filter(Posts.category=='test')
#     posts = Posts.query.all()
#     last = math.ceil(len(posts) / int(params['no_of_posts']))
#
#     # [0:params['no_of_posts']]
#     # PAGINATION Logic
#     page = request.args.get('page')
#     if (not str(page).isnumeric()):
#         page = 1
#     page = int(page)
#     posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
#         params['no_of_posts'])]
#     if (page == 1):
#         prev = '#'
#         next = "/showinfo?page=" + str(page + 1)
#     elif (page == last):
#         prev = "/showinfo?page=" + str(page - 1)
#         next = '#'
#     else:
#         prev = "/showinfo?page=" + str(page - 1)
#         next = "/showinfo?page=" + str(page + 1)
#
#     # print(posts)
#     return render_template('showinfo.html', params=params, posts=posts, prev=prev, next=next)