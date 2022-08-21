from flask import Flask, request

import numpy as np
import joblib

app = Flask(__name__)

model_file = 'model/model.pkl'
model = joblib.load(model_file)

COLUMNS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
CLASSES = ['setosa', 'versicolor', 'virginica']

@app.route('/health', methods=['GET'])
def health():
    return {
        'status': 200,
    }

@app.route('/predict', methods=['GET'])
def predict():
    feature_dict = request.get_json()
    x = [feature_dict[col] for col in COLUMNS]
    x = np.array(x).reshape(1, -1)
    pred = model.predict(x)[0]

    return {
        'status': 2000,
        'class': CLASSES[pred]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)