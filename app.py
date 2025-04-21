from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


# import the models
rf_model = pickle.load(open('models/random_forest.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))
feature_names = scaler.feature_names_in_


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        FFMC = float(request.form.get('FFMC'))
        Rain = float(request.form.get('Rain'))
        ISI = float(request.form.get('ISI'))
        DMC = float(request.form.get('DMC'))
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Sidi_Bel_Abbes = float(request.form.get('Sidi-Bel Abbes'))

        datapoint = pd.DataFrame({'Sidi-Bel Abbes': [Sidi_Bel_Abbes],
                          'Temperature': [Temperature],
                          'RH': [RH],
                          'Ws': [Ws],
                          'Rain': [Rain],
                          'FFMC': [FFMC],
                          'DMC': [DMC],
                          'ISI': [ISI]})
        
        new_data_scaled=scaler.transform(datapoint[feature_names])
        result=rf_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0]) 
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')