from flask import Flask, render_template, request 
import utils

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/predict/', methods=['GET', 'POST'])
def predict():  
    if request.method == 'POST': 
        Gender = request.form.get('Gender')
        Married = request.form.get('Married')
        Education = request.form.get('Education')
        Self_Employed = request.form.get('Self_Employed')  
        ApplicantIncome = float(request.form.get('ApplicantIncome'))  # Convert to float
        CoapplicantIncome = float(request.form.get('CoapplicantIncome'))  # Convert to float
        LoanAmount = float(request.form.get('LoanAmount'))  # Convert to float
        Loan_Amount_Term = float(request.form.get('Loan_Amount_Term'))  # Convert to float
        Credit_History = float(request.form.get('Credit_History'))  # Convert to float
        Property_Area = request.form.get('Property_Area')  

        # Call preprocessdata function with the provided data
        prediction = utils.preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                                           CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                                           Property_Area)

        return render_template('predict.html', prediction=prediction) 
    else:
        return render_template('predict.html')  # Render the form template for GET requests

if __name__ == '__main__': 
    app.run(debug=True)
