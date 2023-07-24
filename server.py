from flask import Flask, request,jsonify
from flask_cors import CORS  # Import CORS module

import utility

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_columns')
def get_columns():
    response = utility.get_data_columns()
    return response

@app.route('/loan_status', methods=['POST'])
def loan_status():
    # Retrieve form data from the request
    Gender = request.form['Gdr']
    Married = request.form['Mrd']
    Dependents = request.form['dpnts']
    Education = request.form['Edc']
    Self_Employed = request.form['SE']
    ApplicantIncome = request.form['Apinc']
    CoapplicantIncome = request.form['Coapinc']
    LoanAmount = request.form['LAmnt']
    Loan_Amount_Term = request.form['LAT']
    Credit_History = request.form['CrHtry']
    Property_Area = request.form['PprAr']

    # Make the loan status prediction
    status = utility.predict_loan_status(Gender, Married, Dependents, Education, Self_Employed,
                                         ApplicantIncome, CoapplicantIncome, LoanAmount,
                                         Loan_Amount_Term, Credit_History, Property_Area)[0]

    response = jsonify({"loan_status" : status })
    return response

if __name__ == '__main__':
    app.run()
