from flask import Flask, request, render_template
import pickle

app= Flask(__name__)

@app.route('/')

def first():
    return render_template('index.html')

@app.route('/predict')
def predict():


    load_model=pickle.load(open(r'C:\Users\mohit\Downloads\My_Proj\model.pkl', 'rb'))
    Pregnancies=3
    Glucose= 120 
    BloodPressure= 135 
    SkinThickness= 45 
    Insulin= 80 
    BMI= 24 
    DiabetesPedigreeFunction= 0.67 
    Age= 24

    prediction=["non-diabetes","diabetes"]
    result=load_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age]])
    print(f"{prediction[result[0]]}")

    return {"Prediction": prediction[result[0]]}


@app.route('/get_data',methods= ['POST'])
def get_data():
    data= request.form
    print(f"Data={data}")

    Pregnancies= float(data['Pregnancies'])
    Glucose=  float(data['Glucose'])
    BloodPressure=  float(data['BloodPressure'])
    SkinThickness= float(data['SkinThickness'])
    Insulin= float(data['Insulin'])
    BMI= float(data['BMI'])
    DiabetesPedigreeFunction= float(data['DiabetesPedigreeFunction'])
    Age= float(data['Age'])
    user_input=[[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age]]
    prediction=["non-diabetes","diabetes"]
    load_model=pickle.load(open(r'C:\Users\mohit\Downloads\My_Proj\model.pkl', 'rb'))
    result=load_model.predict(user_input)
    
    return {"Prediction": prediction[result[0]]}

# @app.route('/get_data', methods=['POST'])
# def get_data():
#     if request.method == 'POST':
#         data = request.form
#         print(f"Data={data}")
#         return "Data captured from Postman"
#     else:
#         return "Use POST method to send data"

    

if __name__ == "__main__":
    app.run(debug=True)


