from flask import Flask, request, jsonify
import joblib
import json
import numpy as np
from flask_cors import CORS  # Import CORS


# Initialize the Flask app
app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

# Load the trained Naive Bayes model
model = joblib.load('models/categorical_naive_bayes_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.json

    # Extract features from the JSON data 
    features = np.array(json.loads(data['features'])).reshape(1, -1)

    # Use the loaded model to make a prediction
    prediction = model.predict(features)

    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
