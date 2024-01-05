from flask import render_template,request
from twitter import app
from twitter.forms import TweetForm
import pickle

@app.route('/',methods=['GET','POST'])
def home():
    form  = TweetForm()
    return render_template('home.html',form=form)