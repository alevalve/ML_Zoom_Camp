import pickle

from flask import Flask
from flask import request
from flask import jsonify

def clean(grade, dv, model):
    
    grade = request.get_json()
    X = dv.transform([grade])
    y_pred = model.predict(X)
    return y_pred

model_file = "lar.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('prediction')
@app.route('/prediction', methods=['POST'])

def predict():
    customer = request.get_json()

    prediction = clean(customer, dv, model)
    result = {
        'grade': float(prediction)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
    
