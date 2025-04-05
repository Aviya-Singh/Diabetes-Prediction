import numpy as np
import pickle
from flask import Flask, request, render_template

# Define a flask app
app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

print('Model loaded. Start serving...')
print('Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        age = request.form['age']
        gender = request.form['gender']
        Polyuria = request.form['Polyuria']
        Polydipsia = request.form['Polydipsia']
        Weight = request.form['Weight']
        Weakness = request.form['Weakness']
        Polyphagia = request.form['Polyphagia']
        Thrush = request.form['Thrush']
        Blurring = request.form['Blurring']
        Itching = request.form['Itching']
        Irritability = request.form['Irritability']
        Healing = request.form['Healing']
        Paresis = request.form['Paresis']
        Stiffness = request.form['Stiffness']
        Alopecia = request.form['Alopecia']
        Obesity = request.form['Obesity']
        
        # Convert form data to appropriate types
        newpat = [[int(age), int(gender), int(Polyuria), int(Polydipsia), 
                  int(Weight), int(Weakness), int(Polyphagia), int(Thrush),
                  int(Blurring), int(Itching), int(Irritability), int(Healing),
                  int(Paresis), int(Stiffness), int(Alopecia), int(Obesity)]]
        
        # Make prediction
        result = model.predict(newpat)
        print(result)
        
        if result[0] == 1:  # Accessing the first element of the result array
            val = "Diabetes"
        else:
            val = "No Diabetes"
        
        return render_template('index.html', value=val)
    
    # For GET request, just show the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)