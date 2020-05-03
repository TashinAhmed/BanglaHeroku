import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import webtool

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = True

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/predict',methods=['post'])
def predict():
    '''For rendering results on HTML GUI'''
    inputs = request.form.values()
    input_lists = webtool.convert(inputs)
    output = []
    if len(input_lists) != 0:
        for i in input_lists:
            output.append(webtool.fun(i))
        # inputs = 0
        input_lists.clear()
    else:
        return render_template("index.html",prediction_text = len(input_lists))
    
    return render_template("index.html", prediction_text = output)
if __name__ == "__main__":
    app.run(debug=True)
