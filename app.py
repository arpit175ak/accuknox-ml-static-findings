from flask import Flask, request
import pickle
import os

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

@app.route("/debug")
def debug():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

app.run(host="0.0.0.0", port=5000, debug=True)
