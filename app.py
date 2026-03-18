from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validation — check all required fields exist
    required_fields = ['Pregnancies', 'Glucose', 'BloodPressure', 
                       'SkinThickness', 'Insulin', 'BMI', 
                       'DiabetesPedigreeFunction', 'Age']
    
    for field in required_fields:
        if field not in data:
            return jsonify({
                'error': f'Missing field: {field}'
            }), 400

    sample = pd.DataFrame([data])
    prediction = model.predict(sample)[0]
    result = 'Has Diabetes' if prediction == 1 else 'No Diabetes'
    return jsonify({'prediction': result})

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)