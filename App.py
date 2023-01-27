from flask import Flask, render_template, request, app, jsonify, url_for
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load("Final Model.sav")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict-api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    new_data = data
    print(new_data)
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=np.reshape(data, (1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    if output:
        return render_template("home.html",prediction_text="Patient is Suffering from Heart Disease")
    else:
        return render_template("home.html",prediction_text="Patient is Not Suffering from Heart Disease")

if __name__ == '__main__':
    app.run(debug=True)