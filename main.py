
from flask import Flask, render_template, request
import requests
import jsonify
import pickle
import numpy as np
import sklearn

app = Flask(__name__,template_folder='templates')


with open ('species_pickle' , 'rb') as f:
    MODEL=pickle.load(f)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Weight = float(request.form['Weight'])
    Length1 = float(request.form['Length1'])
    Length2 = float(request.form['Length2'])
    Length3 = float(request.form['Length3'])
    Height = float(request.form['Height'])
    Width = float(request.form['Width'])
    prediction=MODEL.predict([[Weight,Length1,Length2,Length3,Height,Width]])
    output=prediction
    return render_template('result.html',prediction="The prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)
