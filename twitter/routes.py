from flask import render_template,request
from twitter import app
from twitter.forms import TweetForm
import pickle
import warnings
warnings.filterwarnings("ignore")

@app.route('/',methods=['GET','POST'])
def home():
    form  = TweetForm()
    predicted_value=''
    if request.method == 'POST':
        mfile = open('model/model_pickle','rb')
        vfile = open('model/vectorizer_pickle','rb')
        model = pickle.load(mfile)
        vectorizer = pickle.load(vfile)
        vector = vectorizer.transform([form.tweet.data])
        form.tweet.data = ""
        predicted_value = model.predict(vector)[0]
        mfile.close()
        vfile.close()
        return render_template('home.html',form=form,predicted_value=predicted_value)
    return render_template('home.html',form=form)