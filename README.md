# 🔥 Algerian Forest Fire Prediction App

This project is a machine learning-based web application for predicting the likelihood of a forest fire in Algeria using weather and fire index data. It utilizes a **Random Forest Classifier** and is deployed via a **Flask web app**.

## 📊 Dataset Overview

The dataset includes meteorological and fire weather indices collected from June to September 2012. It contains two classes:

- **Fire**: Indicates the presence of a forest fire
- **not Fire**: Indicates no fire occurred

### ✅ Features Used

| Feature | Description |
|--------|-------------|
| Date   | Day, month, and year (DD/MM/YYYY) |
| Temp   | Temperature at noon (22°C to 42°C) |
| RH     | Relative Humidity in % (21% to 90%) |
| Ws     | Wind speed in km/h (6 to 29) |
| Rain   | Rainfall in mm (0 to 16.8) |
| FFMC   | Fine Fuel Moisture Code (28.6 to 92.5) |
| DMC    | Duff Moisture Code (1.1 to 65.9) |
| DC     | Drought Code (7 to 220.4) |
| ISI    | Initial Spread Index (0 to 18.5) |
| BUI    | Buildup Index (1.1 to 68) |
| FWI    | Fire Weather Index (0 to 31.1) |

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Target variable:** `Classes` (Fire / not Fire)
- **Preprocessing:** Feature selection, data cleaning, label encoding
- **Model Evaluation:** Accuracy

---

## 🌐 Web App (Flask)

The app takes user inputs for all the features and predicts whether a fire is likely to occur.

