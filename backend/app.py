from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model, scaler, and label encoder
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    features = [float(x) for x in request.form.values()]
    data = np.array([features])

    # Scale the data
    scaled_data = scaler.transform(data)

    # Make a prediction
    prediction_encoded = model.predict(scaled_data)
    prediction = label_encoder.inverse_transform(prediction_encoded)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
