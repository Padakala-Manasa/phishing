from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import tldextract
import os

app = Flask(__name__)
CORS(app)

# Paths to the model and vectorizer
model_path = './models/model.pkl'
vectorizer_path = './models/vectorizer.pkl'

# Load the model and vectorizer
model = None
vectorizer = None

try:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    with open(vectorizer_path, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    print("Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if not model or not vectorizer:
        return jsonify({"error": "Model or vectorizer not loaded"}), 500

    try:
        # Extract domain features from URL
        domain_info = tldextract.extract(url)
        processed_url = f"{domain_info.domain}.{domain_info.suffix}"

        # Transform using vectorizer
        url_vectorized = vectorizer.transform([processed_url])

        # Predict
        prediction = model.predict(url_vectorized)[0]
        result = "Legitimate" if prediction == 0 else "Phishing"

        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True, port=5000)