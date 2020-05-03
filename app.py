import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import webtool

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = False

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    '''For rendering results on HTML GUI'''

    inputs = request.form.values()
    input_lists = webtool.convert(inputs)
    
    sentence = ""
    for chunks in input_lists:
        sentence += chunks + ' '
    ouput = []
    if input_lists != 0:
        for i in input_lists:
		output.append(webtool.fun(i))
            
    
    return render_template("index.html", prediction_text = "output " + output, input_text = "input " + sentence)
if __name__ == "__main__":
    app.run(debug=True)
