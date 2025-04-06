import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the saved model
# Make sure 'pipe_model.sav' is in the same directory as this script or update the path accordingly
with open('pipe_model.sav', 'rb') as f:
    pipe_model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Extract height from the request
    height = data['height']
    
    # Predict the weight using the model
    prediction = pipe_model.predict([[height]])
    
    # Return the prediction as a JSON response
    return jsonify({'predicted_weight': prediction[0]})

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)