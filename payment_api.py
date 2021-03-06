# Assumptions while passing the args to the URL:
# 1) Enter amount in float (decimal format)
# 2) Enter Date as dd-mm-yyyy.

# import necessary libraries and functions
from flask import Flask, jsonify, request
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "Welcome to Payment Gateway API. An assignment by Vertika."
    return jsonify({'data': data})


@app.route('/process_payment/<string:CreditCardNumber>/<string:CardHolder>/<path:ExpirationDate>/<string:SecurityCode>/<float:Amount>', methods=['GET', 'POST'])
def process_payment(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
    def valid_test():
        try:

            def ValidTest_CreditCardNumber():  # Validation Test For Credit Card Number
                try:
                    is_success_1 = np.NaN

                    if (type(CreditCardNumber) != str):
                        is_success_1 = 0
                    elif ((pd.isna(CreditCardNumber) == False) and (len(CreditCardNumber) == 16) and (CreditCardNumber.isnumeric() == True)):
                        is_success_1 = 1
                    else:
                        is_success_1 = 0

                    return is_success_1

                except:
                    result_1 = 'ValidTest_CreditCardNumber function failed.\nThe request is invalid: 400 bad request.'

            success_1 = ValidTest_CreditCardNumber()

            def ValidTest_CardHolder(S1):  # Validation Test For Card Holder
                try:
                    if(S1 == 1):
                        is_success_2 = np.NaN

                        if (type(CardHolder) != str):
                            is_success_2 = 0
                        elif (pd.isna(CardHolder) == False) and (CardHolder.isalpha() == True):
                            is_success_2 = 1
                        else:
                            is_success_2 = 0

                        return is_success_2  # return got nothing to return so it goes in except

                except:
                    result_2 = 'ValidTest_CardHolder function failed.\nThe request is invalid: 400 bad request.'

            success_2 = ValidTest_CardHolder(success_1)

            # Validation Test For Expiration Date

            def ValidTest_ExpirationDate(S2):
                try:
                    if(S2 == 1):
                        today = date.today()
                        ExpirationDate_dt = datetime.strptime(
                            ExpirationDate, "%d-%m-%Y").date()
                        is_success_3 = np.NaN

                        if(((pd.isna(ExpirationDate_dt) == False) and (ExpirationDate_dt >= today)) == True):
                            is_success_3 = 1
                        else:
                            is_success_3 = 0

                        return is_success_3

                except:
                    result_3 = 'ValidTest_ExpirationDate function failed.\nThe request is invalid: 400 bad request.'

            success_3 = ValidTest_ExpirationDate(success_2)

            # Validation Test For Security Code
            def ValidTest_SecurityCode(S3):
                try:
                    if(S3 == 1):
                        is_success_4 = np.NaN

                        if (type(SecurityCode) != str):
                            is_success_4 = 0
                        elif ((len(SecurityCode) == 3) and (SecurityCode.isnumeric() == True)):
                            is_success_4 = 1
                        else:
                            is_success_4 = 0

                        return is_success_4

                except:
                    result_4 = 'ValidTest_SecurityCode function failed.\nThe request is invalid: 400 bad request.'

            success_4 = ValidTest_SecurityCode(success_3)

            def ValidTest_Amount(S4):   # Validation Test for Amount
                try:
                    if(S4 == 1):
                        is_success_4 = np.NaN
                        # converting entered amount to decimal type
                        Amount_decimal = float(Amount)

                        if (pd.isna(Amount_decimal) == False) and ((Amount_decimal >= 0) == True):
                            is_success_4 = 1
                        else:
                            is_success_4 = 0

                        return is_success_4
                except:
                    result_5 = 'ValidTest_Amount function failed.\nThe request is invalid: 400 bad request.'

            success_5 = ValidTest_Amount(success_4)

            return success_1, success_2, success_3, success_4, success_5
        except:
            result_all_valid = 'All_1 the validation functions failed.\nThe request is invalid: 400 bad request.'

    result_valid_test = valid_test()

    # Creating the Payment Gateways

    def CheapPaymentGateway():
        return 'Payment is processed: 200 OK'

    def ExpensivePaymentGateway():
        return 'Payment is processed: 200 OK'

    def PremiumPaymentGateway():
        is_processed = 1  # This means Payment is successful using PPG
        return is_processed  # returning true to Highamount method

    # Assigning the Payment Gateways

    def MediumAmount():
        try:
            if callable(ExpensivePaymentGateway):
                result_EPG = ExpensivePaymentGateway()
                return result_EPG
            elif trial == 1:
                result_CPG = CheapPaymentGateway()
                return result_CPG

        except:
            print('Error:500 internal server error')

    def HighAmount():
        try:
            i = 1
            while (i <= 4):
                i = i+1
                success = PremiumPaymentGateway()

                if success == 1:
                    result_PPG = 'Payment is processed: 200 OK'
                    return result_PPG
                    break

        except:
            print('Error:500 internal server error')

    # Here we are checking the amount entered by the user and assigning the payment gateways accordingly.
    try:
        if((max(result_valid_test) == 1) and (min(result_valid_test) == 1)):
            if Amount <= 20:
                result_5 = CheapPaymentGateway()
                return result_5
            elif 21 <= Amount < 500:
                result_6 = MediumAmount()
                return result_6
            else:
                result_7 = HighAmount()
                return result_7
    except:
        result_8 = 'The request is invalid: 400 bad request'
        return result_8


if __name__ == '__main__':
    app.run(debug=True)
