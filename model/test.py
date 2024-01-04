import pickle

fm = open('model_pickle','rb')
model = pickle.load(fm)

fv = open('vectorizer_pickle','rb')
vectorizer = pickle.load(fv)

tweet = input("Enter the tweet: ")
X = vectorizer.transform([tweet])
print(f"Predicted Sentiment: {model.predict(X)[0]}")