"""-- Movie App Created by Faith Akosile"""
from base64 import decode
import os
from pickletools import string1
import random

import json
from re import I
import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    current_user,
    logout_user,
)
from login import loginforms
from models import db, userlogin, ratings
from moviedata import getmovie

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url")
app.config["SECRET_KEY"] = os.getenv("api_secret")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
login_manager = LoginManager()  # is for the flask login extension
login_manager.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()  # this creates the database from models


@app.route("/", methods=["GET", "POST"])  # could be signup page
def home():
    """This is the Home page"""
    return flask.render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """This creates sign up and inserts into database."""
    if flask.request.method == "POST":
        data = flask.request.form  # this is to get the html form data
        passdata = flask.request.form
        newuser = userlogin(username=data["enteruser"])
        newpass = userlogin(password=passdata["enterpass"])
        if (
            userlogin.query.filter_by(username=newuser.username).first()
            is None  # change this
            and userlogin.query.filter_by(password=newpass.password).first() is None
        ):
            entry = userlogin(username=newuser.username, password=newpass.password)
            db.session.add(entry)
            db.session.commit()
            return flask.redirect("/")

    return flask.render_template("signup.html")
    # return  flask.render_template("signup.html")


@login_manager.user_loader
def loaduser(user_id):
    """."""
    return userlogin.query.get(user_id)
    # db.session.query(userlogin).get(id)

    # shows = userlogin.query.all()  # if its a dead call just call it
    # for show in shows:
    #   show = show.id
    # return userlogin.query.get(int(show))  # this gets the row id


@app.route("/submit", methods=["GET", "POST"])  # login
def submit():
    form = loginforms()
    if form.validate_on_submit():
        data = flask.request.form  # this is to get the html form data
        passdata = flask.request.form
        alreadyuser = userlogin(username=data["users"])
        alreadypass = userlogin(password=passdata["passw"])
        iduser = userlogin.query.filter_by(
            username=alreadyuser.username
        ).first()  # i am trying to check if the id matches i am supposed to filter by
        # print(iduser, alreadypass)
        if iduser is not None:

            login_user(iduser)
            print(login_user(iduser))

            return flask.redirect("/getmovie")
        flask.flash("You have entered the wrong login!")

    return flask.render_template("login.html", form=form)


@app.route("/getmovie", methods=["GET", "POST"])
@login_required
def getm():
    """This is the get movie method."""
    id_list = [
        157336,
        585083,
        774825,
        524434,
        860623,
        624860,
        635302,
        644495,
        860623,
        580489,
        811592,
        425909,
        766907,
        843241,
        566525,
        892153,
        637649,
        646385,
        476669,
        597208,
        568124,
        783461,
        800510,
        615904,
    ]  # add more ids!!
    index = random.choice(id_list)
    # print("here")
    # print(index)
    movie = getmovie(index)

    if flask.request.method == "POST":
        data = flask.request.form
        rating = data["rating"]
        comment = data["commentsection"]
        myid = movie["movieid"]
        record = ratings(score=rating, comments=comment, mov_id=myid)
        db.session.add(record)
        db.session.commit()
    myid = movie["movieid"]
    id_movie = ratings.query.filter_by(mov_id=myid).all()

    rate_score = 0
    usercomments = []
    userids = []
    for record in id_movie:
        rate_score += record.score / 10
        name = userlogin.query.filter_by(id=record.user_id).first().username
        usercomments.append(f"{record.comments}~{name}")
        userids.append(record.user_id)
        print(rate_score)

    commentslength = len(usercomments)

    return flask.render_template(
        "movies.html",
        title=movie["title"],
        tag=movie["tag"],
        genlist=movie["genlist"],
        pic=movie["pic"],
        wikipage=movie["wikipage"],
        usercomments=usercomments,
        rate_score=rate_score,
        myid=myid,
        user=current_user.id,
        commentslength=commentslength,
        userids=userids,
    )


@app.route("/rate", methods=["GET", "POST"])
@login_required
def rate():
    """This is the get movie method."""
    if flask.request.method == "POST":
        data = flask.request.form
        rating = data["rating"]

        comment = data["commentsection"]
        myid = data["myid"]
        movie = getmovie(myid)
        record = ratings(
            score=rating, comments=comment, mov_id=myid, user_id=current_user.id
        )
        # record.user_id = current_user.id
        db.session.add(record)
        db.session.commit()
    if flask.request.form.get("deletebutton", False) == "Delete Comment":
        a = ratings.query.filter_by(score=record.score, user_id=record.user_id).first()
        db.session.delete(a)
        db.session.commit()

    myid = data["myid"]

    id_movie = ratings.query.filter_by(mov_id=myid).all()
    rate_score = 0

    usercomments = []
    userids = []
    for record in id_movie:
        rate_score += record.score / 10
        name = userlogin.query.filter_by(id=record.user_id).first().username
        usercomments.append(f"{record.comments}~{name}")
        userids.append(record.user_id)
        print(rate_score)

    commentslength = len(usercomments)

    return flask.render_template(
        "ratings.html",
        title=movie["title"],
        tag=movie["tag"],
        genlist=movie["genlist"],
        pic=movie["pic"],
        wikipage=movie["wikipage"],
        usercomments=usercomments,
        user=current_user.id,
        commentslength=commentslength,
        userids=userids,
        rate_score=rate_score,
        # commentsandratings=commentsandratings
        # givecomment=givecomment
        # testname=testname,
    )


# create a js file that fetches just the givecomment nothing else


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return flask.redirect("/")


app.run(
    host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True
)
