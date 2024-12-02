from flask import Flask, render_template, request, flash
import pickle
import numpy as np

app = Flask(__name__)
app.logger.setLevel('INFO')  # Set the logging level to INFO
app.secret_key = 'Kabwire'  

# Load the trained model
with open('Tuned Logistic Regression Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the standard scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Define the feature names
            feature_names = [
                'BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES',
                'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
                'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS',
                'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE'
            ]

            # Get input features from the form
            features = [float(request.form[feature]) for feature in feature_names]

            # Validate inputs
            if not all(np.isfinite(features)):
                raise ValueError("Invalid input. Please enter valid numeric values.")

            # Scale the input features using the loaded scaler
            scaled_features = scaler.transform([features])

            # Make prediction
            prediction = model.predict(scaled_features)

            # Render the result page with the predicted segment
            return render_template('result.html', prediction=prediction[0])

        except Exception as e:
            flash(f"An error occurred: {str(e)}", category='error')
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
