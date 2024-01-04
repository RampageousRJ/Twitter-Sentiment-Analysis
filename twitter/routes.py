from twitter import app

@app.route('/',methods=['GET','POST'])
def home():
    return "<h1>Home Page</h1>"