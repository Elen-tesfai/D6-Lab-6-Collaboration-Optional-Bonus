# Model Prediction API- elen 

# Lab 6: Machine Learning Model Deployment (Optional/Bonus)

This repository contains the code and instructions for deploying machine learning models as web APIs using Flask. The models provide predictions based on input data, and the APIs can be accessed locally on your machine.

The repository includes two main projects:
1. **D6: Lab 6 Collaboration (Optional/Bonus)** – Deploying a model for weight prediction and Iris flower classification.
2. **Lab 6: Deploying a Model (Optional Bonus)** – Deploying a model to predict weight based on height.

Both projects leverage Flask to serve trained machine learning models via REST APIs.

---

## 1. **D6: Lab 6 Collaboration (Optional/Bonus)**

### **Overview**
In this project, we used Flask to create a local web service that predicts output based on two trained machine learning models. The models are served via a REST API and are accessible locally at `http://127.0.0.1:5000/`. This API provides a POST endpoint for making predictions.

The two models included are:
- A **Linear Regression Model** that predicts weight based on height.
- A **Logistic Regression Model** that classifies Iris flowers based on four features (sepal length, sepal width, petal length, and petal width).

### **Files Provided**
- **lab6_starter.ipynb**: A Jupyter Notebook containing the starter code and initial data exploration.
- **app.py**: The Flask app that serves the machine learning model and handles incoming requests.
- **height_weight_model.sav**: A trained Linear Regression model to predict weight based on height.
- **iris_model.sav**: A trained Logistic Regression model to classify Iris flowers.

### **Steps Taken**
1. **Download and Setup**
   - Download the necessary files: `Lab W6 SciKit.pdf`, `lab6_starter.ipynb`, and `app.py`.
   
2. **Modifications**
   - Modified the `app.py` script to:
     - Serve the trained models for predictions.
     - Accept input in JSON format via the `/predict` endpoint.

3. **Running the App**
   - Run the Flask app locally by executing `python app.py` in the terminal.
   - Access the app in a browser via `http://127.0.0.1:5000/`.

4. **Testing the API**
   - Test the API using `Invoke-WebRequest` on PowerShell to send POST requests and receive predictions from the model.

### **How to Run**
1. Clone the repository or download the files directly.
2. Install the required dependencies:
   ```bash
   pip install Flask==2.2.3
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
```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"input": [5.1, 3.5, 1.4, 0.2]}'
```
Example response:
{
  "prediction": [0]
}

#### Request 2:
Send a POST request with input data for the height-to-weight prediction model.
```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"input": [160]}'
```
Example response:
{
  "prediction": [60.0]
}

Result Example:

PS C:\Users\su_te> Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"input": [160]}'

StatusCode        : 200
StatusDescription : OK
Content           : {
                      "prediction": [
                        60.0
                      ]
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 35
                    Content-Type: application/json
                    Date: Fri, 04 Apr 2025 06:20:49 GMT
                    Server: Werkzeug/3.1.3 Python/3.10.11

                    {
                      "prediction": [
                        60.0
                      ]
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 35], [Content-Type, application/json], [Date, Fri, 04 Apr 2025 06:20:49 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 35


PS C:\Users\su_te> Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"input": [5.1, 3.5, 1.4, 0.2]}'

StatusCode        : 200
StatusDescription : OK
Content           : {
                      "prediction": [
                        0
                      ]
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 32
                    Content-Type: application/json
                    Date: Fri, 04 Apr 2025 06:21:05 GMT
                    Server: Werkzeug/3.1.3 Python/3.10.11

                    {
                      "prediction": [
                        0
                      ]
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 32], [Content-Type, application/json], [Date, Fri, 04 Apr 2025 06:21:05 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 32

### Explanation:
- **GET Request**: Used to check if the API is live and running.
- **POST Request**: Used to send input data to the server, which will return predictions based on the trained models.


## 2. Lab 6: Deploying a Model (Optional Bonus)

### Overview

In this project, we deployed a model for predicting weight based on height using Flask. This model was trained on a dataset provided in `data.csv`. The trained model is served as a pipeline using the saved model file `pipe_model.sav`. The API can be accessed locally via `http://127.0.0.1:5000/` and provides a POST endpoint for predictions.

### Files Provided

- **Elen_Lab6_Model_Deployment.ipynb**: Jupyter Notebook containing the data preprocessing, model training, and pipeline creation.
- **app.py**: Flask app that serves the trained model and handles incoming requests.
- **convert_encoding.py**: Python script for data preprocessing.
- **data.csv**: Dataset used for training the model.
- **pipe_model.sav**: The trained pipeline model for predicting weight based on height.

### Steps Taken

#### 1. Download and Setup

Download the necessary files: 
- `Elen_Lab6_Model_Deployment.ipynb`
- `app.py`
- `convert_encoding.py`
- `data.csv`
- `pipe_model.sav`

#### 2. Model Training

In `Elen_Lab6_Model_Deployment.ipynb`, we trained a **Linear Regression** model to predict weight based on height using `data.csv`. The model was saved as a pipeline in `pipe_model.sav`.

#### 3. Flask API Development

We modified `app.py` to:
- Load the saved pipeline model (`pipe_model.sav`).
- Set up a **Flask API** that listens for POST requests.
- Serve the model's predictions via the `/predict` endpoint.

#### 4. Running the App

The Flask app was run locally by executing:

```bash
python app.py
  ```
  ### The app was accessed in a browser via `http://127.0.0.1:5000/`.

### 5. Testing the API

Test the API using **Invoke-WebRequest** on PowerShell to send POST requests and receive predictions from the model.

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"height": 170}'
```
### Testing the Endpoints

#### GET Request (To check if the API is live)

In PowerShell, run:

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/" -Method GET
```
### POST Request (To make a prediction)

Send a POST request with input data for the weight prediction model:

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"height": 170}'
```
Example response:
{
  "predicted_weight": 70.0
}

Result Example:

PS C:\Projects\flask_model_deployment\Lab6-Model-Deployment> Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"height": 170}'

StatusCode        : 200
StatusDescription : OK
Content           : {
                      "predicted_weight": 70.0
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 31
                    Content-Type: application/json
                    Date: Sat, 05 Apr 2025 17:35:09 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.0

                    {
                      "predicted_weight": 70.0
                    }

## **Conclusion**

### **1. D6: Lab 6 Collaboration (Optional/Bonus)**

In this lab, I successfully deployed two machine learning models as web services using Flask. The deployment process involved creating a Flask API that could serve predictions from both models via HTTP requests.

The two models deployed are:

- **Weight Prediction Model:** A linear regression model predicting weight based on height. For example, with a height of 160 cm, the predicted weight was 60 kg.
- **Iris Flower Classification Model:** A logistic regression model classifying flowers based on features. For input `[5.1, 3.5, 1.4, 0.2]`, it predicted class "0".

This exercise helped me learn how to deploy models via APIs for real-time predictions.

---

### **2. Lab 6: Deploying a Model (Optional Bonus)**

I deployed a weight prediction model based on height using Flask. The model was trained and saved as a pipeline (`pipe_model.sav`). The app allowed users to send POST requests, and for a height of 170 cm, the predicted weight was 70 kg.

This lab provided hands-on experience in deploying machine learning models via APIs and helped me understand Flask for real-time predictions