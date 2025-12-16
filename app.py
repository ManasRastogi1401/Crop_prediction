import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    # The output of model.predict is an array, so get the first item
    return render_template("index.html", prediction_text = "The Predicted Crop is {}".format(prediction[0]))

if __name__ == "__main__":
    # RENAMED this variable
    app.run(debug=True)
