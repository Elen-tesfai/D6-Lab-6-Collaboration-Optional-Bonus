from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load both models
model_1 = pickle.load(open('height_weight_model.sav', 'rb'))  # Linear Regression model for height-weight
iris_model = pickle.load(open('iris_model.sav', 'rb'))  # Logistic Regression model for Iris dataset

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get JSON data from the request
        
        if 'input' in data:
            # Check if the input contains a list for prediction
            input_data = np.array(data['input']).reshape(1, -1)  # Convert input to a numpy array and reshape if needed

            # For height-weight model (if input length is 1)
            if len(data['input']) == 1:
                prediction = model_1.predict(input_data)  # Predict with height_weight_model
                return jsonify({'prediction': prediction.tolist()})

            # For Iris model (if input length is 4, assuming Iris dataset with 4 features)
            elif len(data['input']) == 4:
                prediction = iris_model.predict(input_data)  # Predict with iris_model
                return jsonify({'prediction': prediction.tolist()})
        
        # Handle invalid input
        return jsonify({'error': 'Invalid input. Provide either 1 (for height) or 4 (for Iris features) inputs.'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)