from flask import Flask, render_template, request, session, redirect, flash
# imported flask-alchemy to creation of the db
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json
import math

'''why-with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams'''
# making params configurable
with open('config.json', 'r') as c:
    params = json.load(c)['params']
local_server = True

# fllowing is the syntax to be follwed for creating app of sql avalible on
app = Flask(__name__)
app.secret_key = 'super-secret-key'
# following is the synatx for gmail smtp server config
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail_username'],
    MAIL_PASSWORD=params['gmail_pass']
)
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

# url for connecting with mysqli=mysql://username:password@localhost/db_name
db = SQLAlchemy(app)

# creating the class for contacts table linking with myqli


class Contacts(db.Model):
    '''srno,name,email,phone_number,message,date
    email = db.Column(db.String(12), unique=True, nullable=False)
    syntax to be flwd  abve'''
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=False)
    email = db.Column(db.String(12), unique=True, nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Posts(db.Model):
    '''srno,name,email,phone_number,message,date
    email = db.Column(db.String(12), unique=True, nullable=False)
    syntax to be flwd  abve'''
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(18), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    tag_line = db.Column(db.String(80), nullable=False)
    img_file = db.Column(db.String(25), nullable=True)
    date = db.Column(db.String(12), nullable=True)


@app.route('/')
def home():
    '''logic for pagination
    #first-
     prev=#
     next=page+1
    #middle-
     prev=page-1
     next=page+1
    #last-
    prev=page-1
    next=#

     '''
    posts = Posts.query.filter_by().all()  # to fetch the post and display in homepage
    last = math.ceil(len(posts))/int(params['no_of_posts'])

    page = request.args.get('page')

    if (not str(page).isnumeric()):
        page = 1
        # slicng-
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']):(page-1) *
                  int(params['no_of_posts'])+int(params['no_of_posts'])]
    # first-
    if(page == 1):
        prev = '#'
        next = '/?page=' + str(page + 1)
    # condions for last
    elif (page == last):
        next = '#'
        prev = '/?page=' + str(page - 1)
    # conditions of midlle phase
    else:
        prev = '/?page=' + str(page - 1)
        next = '/?page=' + str(page + 1)

    # name = request.args.get("name", "World")
    return render_template('index.html', params=params, posts=posts, next=next, prev=prev)


# here i created about.html with the help of bootstrap
@app.route('/about')
def about():
    # name = request.args.get("name", "World")
    # name = 'aditya'
    return render_template('about.html', params=params)


@app.route('/login', methods=['GET', 'POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_pass']):
            # to set the seesion variables
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    return render_template('login.html', params=params)


@app.route('/edit/<string:srno>', methods=['GET', 'POST'])
def edit(srno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tag_line = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img')
            date = datetime.now()
        # here we creating the conditions that if no post and the mobe to post.html
            if srno == '0':
                post = Posts(title=box_title, tag_line=tag_line,
                             slug=slug, content=content, img_file=img_file, date=date)
                # above i have assigned the above if cond vars with class Posts vars
                db.session.add(post)
                db.session.commit()
            else:
                '''here i have done the same above condtion assignment with the edit.html name attrbuttes with db posts table'''
                post = Posts.query.filter_by(srno=srno).first()
                post.title = box_title
                post.tag_line = tag_line
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/' + srno)
        post = Posts.query.filter_by(srno=srno).first()
        return render_template('edit.html', params=params, post=post, srno=srno)


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    # name = request.args.get("name", "World")
    # name = 'aditya'
    if (request.method == 'POST'):
        # 'add entry to the db'
        '''here i have the added the name sec in contact.html and to bring them in post method have used below syntax=have fetched the entry '''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # now will add above entries to the db
        entry = Contacts(name=name, email=email,
                         phone_number=phone, message=message, date=datetime.now())
        '''above is used to assign the Contacts class with the entries fetched from the contacts.html
        where,lhs=from db clms and rhs=from def contact.html (name) attribute'''
        # blw queury is to finalize the session
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('new message from ' + name,
        #                   sender=email,
        #                   recipients=[params['gmail_username']],
        #                   body=message + "\n" + phone)
    flash('thanks for connecting with us')
    return render_template('contact.html', params=params)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    # name = request.args.get("name", "World")
    # name = 'aditya'
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params=params, post=post)


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/delete/<string:srno>', methods=['GET', 'POST'])
def delete(srno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(srno=srno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')


app.run(debug=True)
