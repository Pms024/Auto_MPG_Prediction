from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('my_model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Cylinders = float(request.form['Cylinders'])
    Displacement = float(request.form['Displacement'])
    Horsepower = float(request.form['Horsepower'])
    Weight = float(request.form['Weight'])
    Acceleration = float(request.form['Acceleration'])
    Model_Year = float(request.form['Model_Year'])
    Origin = float(request.form['Origin'])
    result = model.predict([[Cylinders,Displacement,Horsepower,Weight,Acceleration,Model_Year,Origin]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
