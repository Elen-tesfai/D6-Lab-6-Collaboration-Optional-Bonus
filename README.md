# Model Prediction API- elen 

This repository contains the code and instructions for deploying a machine learning model as a web API using Flask. The model provides predictions based on input data.

## Project Overview

In this project, we used Flask to create a local web service that predicts output based on two trained machine learning models. The models are served via a REST API and are accessible locally at `http://127.0.0.1:5000/`. This API provides a `POST` endpoint for making predictions. The two models are:
- A **Linear Regression Model** that predicts weight based on height.
- A **Logistic Regression Model** that classifies Iris flowers based on four features (sepal length, sepal width, petal length, and petal width).

## Files Provided

1. **Initial Code**: `lab6_starter.ipynb`
   - A Jupyter Notebook containing the starter code and initial data exploration for the model.
   
2. **Server**: `app.py`
   - The Flask app that serves the machine learning model and handles incoming requests.

3. **Models**:
   - `height_weight_model.sav`: A trained Linear Regression model to predict weight based on height.
   - `iris_model.sav`: A trained Logistic Regression model to classify Iris flowers based on four features.

## Steps Taken

### 1. Download and Setup
   - We started by downloading the necessary files:
     1. `Lab W6 SciKit.pdf`
     2. `lab6_starter.ipynb`
     3. `app.py`

### 2. Modifications
   - We modified the `app.py` script provided by the instructor to create a Flask API that:
     1. Serves the trained model for predictions.
     2. Accepts input in JSON format via the `/predict` endpoint.

### 3. Running the App
   - The Flask app was run locally by executing `python app.py` in the terminal.
   - The app was accessed in a browser via `http://127.0.0.1:5000/`.

### 4. Testing the API
   - We tested the API using `Invoke-WebRequest` on PowerShell to send POST requests and receive predictions from the model.

## How to Run

### 1. Clone the repository or download the files directly.
### 2. Install the required dependencies:
   - `Flask==2.2.3`
### 3. Run the Flask app:
   ```bash
   python app.py
   ```
## 4. Open the browser and test the endpoints.

### 1. GET Request (To check the basic API endpoint)
Use a GET request to confirm that the API is live.

**How to Test:**
In PowerShell, run the following command:

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/" -Method GET
```
### 2. POST Request (To make a prediction)
Use a POST request to send data to the server and receive a prediction.

#### Request 1:
Send a POST request with input data for the Iris flower classification model.

#### Request 2:
Send a POST request with input data for the height-to-weight prediction model.

### Explanation:
- **GET Request**: Used to check if the API is live and running.
- **POST Request**: Used to send input data to the server, which will return predictions based on the trained models.

