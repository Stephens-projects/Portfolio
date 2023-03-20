import numpy as np
from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

model = pickle.load(open('models/grid_lasso.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/nba')
def nba():
    return render_template("nba.html")

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    if int_features[0] > int_features[1] or int_features[2] > int_features[3]:
        return render_template("error.html")
    
    else:
        features = [np.array(int_features)]
        prediction = model.predict(features)
        output = round(prediction[0], 1)
        return render_template("predict.html", prediction_text='Your Players Efficiency is {}'.format(output))

if __name__=="__main__":
    app.run(debug=True)