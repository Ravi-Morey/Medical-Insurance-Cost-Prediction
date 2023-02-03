# from tkinter import BitmapImage
from flask import Flask,jsonify,render_template,request
from utils import MedicalInsurance 
# from distutils.command.config import config
import config
#import jinja2

app = Flask(__name__)

@app.route('/')
def hey_flask():
    #print("welcome to medical insurance charge for u")
    print("********** Your Heath and Reponsibility *************")
    return render_template("index.html")

@app.route('/predict_charges', methods=["GET"])
def get_insurance_charges():

    if request.method == "GET":

        print("we are using a get method")

        # data = request.form
        # print("Data ::",data)
        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']

        age = int(request.args.get("age"))    #type: ignore
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age, sex, bmi, children, smoker, region\n",age,sex,bmi,children,smoker,region)

        medical_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = medical_ins.get_predicted_price()

        return render_template("index.html",prediction=charges)

        return jsonify ({"Result": f"Predicted charges for medical insurance is {charges}/- Rs. Only"})

if __name__=="__main__":
    app.run(host='0.0.0.0', port=7000,debug=True) 
               


