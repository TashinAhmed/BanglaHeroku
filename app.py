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
    inp_lists = ""
    output = ""
    if len(input_lists) != 0:
        for i in input_lists:
            output += webtool.fun(i)
            inp_lists += i + " "
        # inputs = 0
        input_lists.clear()
    else:
        return render_template("index.html",prediction_text = len(input_lists))
    
    return render_template("index.html",input_text = "input: " + inp_lists, prediction_text = "output: " + output)
if __name__ == "__main__":
    app.run(debug=True)
