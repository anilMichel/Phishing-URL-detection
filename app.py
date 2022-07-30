import numpy as np
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import pickle


model = pickle.load(open(r'mnb.pkl', 'rb'))
model1=pickle.load(open(r'count.pkl','rb'))

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        input_dict=request.form.to_dict()
        input_values = input_dict.values()
        print(input_values)
        input_values=str(input_values)
       #input_values = input_values.reshape(-1, 1)
        input_values=input_values.replace('://',' ')
        input_values=input_values.replace('/',' ')
        
        input_values=input_values.replace('.',' ')
        input_values=input_values.replace('?',' ')
        input_values=input_values.replace(',',' ')
        print(input_values)
        input_alues=[input_values]
       # r1=model1.transform(input_values)
        vector = CountVectorizer(vocabulary=model1.vocabulary_)
        vectorizer = vector.fit(input_alues)
        vector = vector.transform(input_alues)#.reshape(-1,1)
        #input_values=np.array(input_values, dtype=float)
        #vector = vector.reshape(1, -1)
        print(vector)
        prediction = model.predict(vector)
        print(prediction)
        pred=""
        if prediction==1:
            pred="this is pishing url please be aware of this type of links"
        else:
            pred="this isafest link"
        return pred
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')