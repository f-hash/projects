# Movie App Summary - by Faith Akosile-
For this assignment, the technologies that were employed include the following: python, python flask, CSS, HTML, PSQL, Flasklogin, Flaskwtfforms,  and JavaScript. The imports that were used include import requests, import os, import JSON, from dotenv import find_dotenv, load_dotenv, import random, load_dotenv(find_dotenv()), import flask, render_template, from flask_sqlalchemy import SQLAlchemy, from dotenv import load_dotenv, find_dotenv, from flask_login import LoginManager, login_required, login_user, from login import loginforms, from models import db, userlogin, ratings, and from moviedata import getmovie. The moviedata.py is a personalized file that gets its information from The Movie DataBase site.
To install the imports above run:
pip install flask-login
pip install -U Flask-WTF

# Forking the Repository:
When forking the repository, the first thing to do is to employ the Heroku create to code an app. The next command is Heroku addons:create heroku-postgresql:hobby-dev -a my app name in order to get a database URL. To get the URL link type Heroku config to get the database URL. Next, code a .env file, place it in the database URL link, and do postgresql instead of postgres at the beginning of the URL link while naming the variable database_url in the .env file. Afterward, place your API key and call it movie_key in the file. Meanwhile, place the secret_key and call it api_secret in the .env file. Next code a .gitignore file, and place .env inside the .gitignore file. After doing the .env file, you have to install the static folder and the templates folder. This must be in the same directory as the app.py, login.py, and moviedata.py.

# How to Run the App
To begin, open the folder that the cloned repository is in and, as mentioned earlier, create the Heroku. The next step in the bash terminal is to run these four commands:
git init
git add -all
git commit -m “App Deployment”
git push Heroku
Executing these commands will deploy the app and run it.

# Experience:
Working on this project was more of an experimental process than I had imagined. Creating the login and signup page was not as difficult as I anticipated, however, I struggled with the rating page. This was because I was still unsure of how to import variables into python. Nevertheless, I enjoyed working on this project because I had the opportunity to explore my styling, especially in comparison to milestone1.
# Applink:
Here is the link to my app: http://mysterious-stream-68205.herokuapp.com/
# SQL - query
For this assignment, I created SQL queries using MySQL in order to manipulate big data for an employee database. I was able to clean the data, manipulate the database and filter the data.
# JAVA - password hash
For this assignment, I implemented a cracker and a dictionary system. For this code, I was able to use the MD5 hash system to check if a password matches the correct hash function.
# Web programming 
For this class, I designed my website using amazon word press or AWS and using a PHP database. The link to the website is http://54.205.139.198/wp-admin

