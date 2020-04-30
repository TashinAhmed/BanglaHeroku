import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import webtool

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = False

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/predict',methods=['post'])
def predict():
    '''For rendering results on HTML GUI'''
    inputs = request.form.values()
    input_lists = webtool.convert(inputs)
    if input_lists == 0:
	output = "enter something in Bangla"
    else:    
	for i in input_lists:
            webtool.MakeError(i)
        output = webtool.listToString(webtool.nlist)
     
    return render_template("index.html", prediction_text=output)
if __name__ == "__main__":
    app.run(debug=True)
