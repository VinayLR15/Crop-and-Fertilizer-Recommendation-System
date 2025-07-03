![Screenshot 2025-07-03 171119](https://github.com/user-attachments/assets/ad8f8dd0-afb0-4326-a172-58358615733b)
# 🌾 Crop and Fertilizer Recommendation System
A Machine Learning-based web application that recommends the most suitable crop and fertilizers based on soil and environmental conditions such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH level, and Rainfall.


## 🚀 Features
- 🌱 Crop recommendation using soil nutrients and weather parameters  
- 🧪 Fertilizer recommendation based on nutrient gaps  
- 📊 Trained ML models using real-world datasets (`Crop_recommendation.csv`, `ferti.csv`)  
- 🖥️ Simple and responsive HTML + CSS frontend  
- 🔧 Powered by Flask backend  
- 📦 Easily deployable on local server or cloud  


## 📂 Project Structure
Crop-and-Fertilizer-Recommendation-System/
├── app.py                      # Flask main application
├── Crop\_recommendation.csv    # Dataset for crop recommendation
├── ferti.csv                  # Dataset for fertilizer mapping
├── crop\_model.pkl             # Trained ML model for crop prediction
├── crop\_encoder.pkl           # Label encoder for crop classes
├── static/                    # Static images and background
│   ├── background3.jpg
│   ├── blacktree.png
│   ├── call4.png
│   ├── colortree.png
├── templates/                 # HTML pages
│   ├── crop.html              # Input form
│   ├── cropresult.html        # Result display


## 🛠️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/VinayLR16/Crop-and-Fertilizer-Recommendation-System.git
cd Crop-and-Fertilizer-Recommendation-System
````

### 2. 📦 Create Virtual Environment and Install Dependencies

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For Linux/Mac

# Install required packages
pip install -r requirements.txt

<sub>If you don't have `requirements.txt`, you can create one like:</sub>

Flask
pandas
scikit-learn

### 3. ▶️ Run the App
python app.py

Open browser and visit: `http://127.0.0.1:5000`


## 🌍 Input Fields (with valid ranges)

| Parameter      | Description             | Expected Range |
| -------------- | ----------------------- | -------------- |
| Nitrogen (N)   | Soil nitrogen content   | 0 – 140        |
| Phosphorus (P) | Soil phosphorus content | 5 – 145        |
| Potassium (K)  | Soil potassium content  | 5 – 205        |
| Temperature    | Air temperature (°C)    | 8 – 45°C       |
| Humidity       | Relative humidity (%)   | 10 – 100%      |
| pH             | Soil pH level           | **0.0 – 14.0** |
| Rainfall       | Rainfall (mm)           | 20 – 300 mm    |

## 🧠 Machine Learning

* Models used: Random Forest Classifier
* Accuracy: \~95% on test data
* Encoders used for label conversion
* Pre-trained `.pkl` files loaded in Flask app

## 📸 Screenshots

| Input Page                       | Output Recommendation Page        |
| -------------------------------- | --------------------------------- |
![image](https://github.com/user-attachments/assets/c34bed4d-f536-4b50-9a12-900e6509d3e8)    ![image](https://github.com/user-attachments/assets/ce22f338-4922-4f53-a03c-6bbd26f93a11)



## 📤 Deployment

You can deploy this Flask app on platforms like:

* **Render** (free Flask deployment)
* **Replit** (runs Flask apps easily)
* **GitHub Pages + Vercel (frontend/backend split)**


## 👤 Author

* **Vinay L R**
* GitHub: [@VinayLR16](https://github.com/VinayLR16)
* Email: [vinaylrvinaylr54@gmail.com](mailto:vinaylrvinaylr54@gmail.com)
