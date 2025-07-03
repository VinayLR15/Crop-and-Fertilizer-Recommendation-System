import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load datasets
crop_data = pd.read_csv('Crop_recommendation.csv')
fertilizer_data = pd.read_csv('ferti.csv')

# Preprocess crop data
crop_X = crop_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
crop_y = crop_data['label']
crop_encoder = LabelEncoder()
crop_y_encoded = crop_encoder.fit_transform(crop_y)

# Train crop recommendation model
crop_X_train, crop_X_test, crop_y_train, crop_y_test = train_test_split(crop_X, crop_y_encoded, test_size=0.2, random_state=42)
crop_model = RandomForestClassifier()
crop_model.fit(crop_X_train, crop_y_train)

# Save crop model and encoder
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(crop_model, f)
with open('crop_encoder.pkl', 'wb') as f:
    pickle.dump(crop_encoder, f)

# Preprocess fertilizer data
fertilizer_X = fertilizer_data[['Nitrogen', 'Phosphorous', 'Potassium']]
fertilizer_y = fertilizer_data['Fertilizer Name']
fertilizer_encoder = LabelEncoder()
fertilizer_y_encoded = fertilizer_encoder.fit_transform(fertilizer_y)

# Train fertilizer recommendation model
fertilizer_X_train, fertilizer_X_test, fertilizer_y_train, fertilizer_y_test = train_test_split(
    fertilizer_X, fertilizer_y_encoded, test_size=0.2, random_state=42)
fertilizer_model = RandomForestClassifier()
fertilizer_model.fit(fertilizer_X_train, fertilizer_y_train)

# Save fertilizer model and encoder
with open('fertilizer_model.pkl', 'wb') as f:
    pickle.dump(fertilizer_model, f)
with open('fertilizer_encoder.pkl', 'wb') as f:
    pickle.dump(fertilizer_encoder, f)

@app.route('/')
def index():
    return render_template('crop.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read input values as float (not int)
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Load saved models and encoders
        with open('crop_model.pkl', 'rb') as f:
            crop_model = pickle.load(f)
        with open('crop_encoder.pkl', 'rb') as f:
            crop_encoder = pickle.load(f)
        with open('fertilizer_model.pkl', 'rb') as f:
            fertilizer_model = pickle.load(f)
        with open('fertilizer_encoder.pkl', 'rb') as f:
            fertilizer_encoder = pickle.load(f)

        # Prepare input for crop prediction
        crop_input = pd.DataFrame([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]],
                                  columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
        crop_prediction = crop_model.predict(crop_input)
        recommended_crop = crop_encoder.inverse_transform(crop_prediction)

        # Prepare input for fertilizer prediction
        fert_input = pd.DataFrame([[nitrogen, phosphorus, potassium]],
                                  columns=['Nitrogen', 'Phosphorous', 'Potassium'])
        fert_prediction = fertilizer_model.predict(fert_input)
        recommended_fertilizer = fertilizer_encoder.inverse_transform(fert_prediction)

        # Render result page
        return render_template('cropresult.html', crops=recommended_crop, fertilizers=recommended_fertilizer)

    except Exception as e:
        import traceback
        return f"<pre>An error occurred:\n{traceback.format_exc()}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
