# -*- coding: utf-8 -*-
"""Credit Score Classification and Loan Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CR_zOGuzSr2Xz1C695yQbtC2HPYcLDE1

***Credit Score Classification and Loan Prediction using Python - ML***
"""



import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("/content/train.xls")

data.head(5)

data.info()

data.isnull().sum()

data['Credit_Score'].value_counts()

"""# Data Exploration"""

fig = px.box(data ,
             x = 'Occupation' ,
             color = 'Credit_Score' ,
             title = 'Credit Scores Based on Occupation' ,
             color_discrete_map ={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.show()

"""There’s not much difference in the credit scores of all occupations mentioned in the data."""

fig = px.box(data ,
             x = 'Credit_Score' ,
             y = 'Annual_Income' ,
             color = 'Credit_Score' ,
             title = 'Credit Scores Based on Annual Income' ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""According to the above visualization, the more you earn annually, the better your credit score is"""

fig = px.box(data ,
             x = "Credit_Score" ,
             y = "Monthly_Inhand_Salary" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on Monthly Inhand Salary" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

"""Like annual income, the more monthly in-hand salary you earn, the better your credit score will become."""

fig = px.box( data ,
             x = "Credit_Score" ,
             y = "Num_Bank_Accounts" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on Number of Bank Accounts" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

"""Maintaining more than five accounts is not good for having a good credit score. A person should have 2 – 3 bank accounts only. So having more bank accounts doesn’t positively impact credit scores."""

fig = px.box( data ,
             x = "Credit_Score" ,
             y = "Num_Credit_Card" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on Number of Credit cards" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

"""Just like the number of bank accounts, having more credit cards will not positively impact your credit scores. Having 3 – 5 credit cards is good for your credit score."""

fig = px.box( data ,
             x = "Credit_Score" ,
             y = "Interest_Rate" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on the Average Interest rates" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""
If the average interest rate is 4 – 11%, the credit score is good. Having an average interest rate of more than 15% is bad for your credit scores."""

fig = px.box( data ,
             x = "Credit_Score" ,
             y = "Num_of_Loan" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on Number of Loans Taken by the Person" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

"""To have a good credit score, you should not take more than 1 – 3 loans at a time. Having more than three loans at a time will negatively impact your credit scores."""



fig = px.box(data,
             x="Credit_Score",
             y="Delay_from_due_date",
             color="Credit_Score",
             title="Credit Scores Based on Average Number of Days Delayed for Credit card Payments",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

"""
So you can delay your credit card payment 5 – 14 days from the due date. Delaying your payments for more than 17 days from the due date will impact your credit scores negatively."""

fig= px.box( data ,
            x = "Credit_Score" ,
            y = "Num_of_Delayed_Payment" ,
            color = "Credit_Score" ,
            title = "Credit Scores Based on Number of Delayed Payments" ,
            color_discrete_map = { 'poor':'red' ,
                                  'standard':'yellow' ,
                                  'good' : 'green' })
fig.update_traces(quartilemethod='exclusive')
fig.show()

"""
So delaying 4 – 12 payments from the due date will not affect your credit scores. But delaying more than 12 payments from the due date will affect your credit scores negatively."""

fig = px.box( data ,
             x = "Credit_Score" ,
             y= "Outstanding_Debt" ,
             color = "Credit_Score" ,
             title = "Credit Scores Based on Outstanding Debt" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""
An outstanding debt of  380-1150 will not affect your credit scores. But always having a debt of more than $1338 will affect your credit scores negatively"""

fig = px.box( data ,
             x = 'Credit_Score' ,
             y = 'Credit_Utilization_Ratio' ,
             color = 'Credit_Score' ,
             title =  "Credit Scores Based on Credit Utilization Ratio" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""Credit utilization ratio means your total debt divided by your total available credit. According to the above figure, your credit utilization ratio doesn’t affect your credit scores"""

fig = px.box( data ,
             x = 'Credit_Score' ,
             y = 'Credit_History_Age' ,
             color= 'Credit_Score' ,
             title = "Credit Scores Based on Credit History Age" ,
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""So, having a long credit history results in better credit scores."""

fig = px.box( data ,
             x = 'Credit_Score' ,
             y = "Total_EMI_per_month" ,
             color = 'Credit_Score' ,
             title = "Credit Scores Based on Total Number of EMIs per Month" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""The number of EMIs you are paying in a month doesn’t affect much on credit scores."""

fig = px.box(data ,
             x='Credit_Score',
             y='Amount_invested_monthly',
             color='Credit_Score',
             title= 'Credit Scores Based on Amount Invested Monthly',
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""The amount of money you invest monthly doesn’t affect your credit scores a lot"""

fig = px.box(data ,
             x = 'Credit_Score' ,
             y = 'Monthly_Balance' ,
             color = 'Credit_Score' ,
             title = "Credit Scores Based on Monthly Balance Left" ,
             color_discrete_map = {'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod = 'exclusive')
fig.show()

"""So, having a high monthly balance in your account at the end of the month is good for your credit scores. A monthly balance of less than $250 is bad for credit scores."""

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1,
                               "Good": 2,
                               "Bad": 0})

from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                   "Num_Bank_Accounts", "Num_Credit_Card",
                   "Interest_Rate", "Num_of_Loan",
                   "Delay_from_due_date", "Num_of_Delayed_Payment",
                   "Credit_Mix", "Outstanding_Debt",
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

# Model Selection Code to see which ML ALgorithm performs better

# # Importing necessary classifiers
# from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


# # List of models with their abbreviations and corresponding instances
# models = [
#     ('LR', LogisticRegression()),                   # Logistic Regression
#     ('NB', GaussianNB()),                           # Naive Bayes
#     ('DT', DecisionTreeClassifier()),               # Decision Tree
#     ('RF', RandomForestClassifier()),               # Random Forest
#     ('GB', GradientBoostingClassifier()),           # Gradient Boosting
#     ('KNN', KNeighborsClassifier()),                # K-Nearest Neighbors
#     ('SVM', SVC()),                                 # Support Vector Machine
#     ('LDA', LinearDiscriminantAnalysis()),          # Linear Discriminant Analysis

# ]

# # Display the list of models
# for name, model in models:
#     print(f"{name}: {model}")
# #

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# # Ensure y is reshaped to a 1D array
# y = y.ravel()

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# # Scale features for better performance
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train and evaluate models
# for name, model in models:
#     clf = model

#     # Adjust LogisticRegression parameters if applicable
#     if name == 'LR':
#         clf.set_params(max_iter=1000)

#     clf.fit(X_train, y_train)
#     accuracy = clf.score(X_test, y_test)
#     print(f"{name}: {accuracy:.4f}")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Ensure y is reshaped to a 1D array
y = y.ravel()

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Scale features for better performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 2) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g,h, i, j,k, l]])
print("Predicted Credit Score = ", model.predict(features))

def predict_loan_amount(credit_score, annual_income, outstanding_debt):
    """
    Predicts loan eligibility based on credit score and financial metrics.
    """
    # Define loan multipliers based on credit score
    loan_multipliers = {
        "Good": 5,       # 5x annual income
        "Standard": 3,   # 3x annual income
        "Bad": 0         # No loan eligibility
    }

    # Get multiplier for credit score
    multiplier = loan_multipliers.get(credit_score, 0)

    # Calculate maximum loan amount
    max_loan = max(0, multiplier * annual_income - outstanding_debt)

    return max_loan


# Example usage:
predicted_credit_score = "Good"  # Example predicted value
annual_income = 100000  # Example input (user-provided)
outstanding_debt = 20000  # Example input (user-provided)

loan_amount = predict_loan_amount(predicted_credit_score, annual_income, outstanding_debt)
print(f"Predicted Loan Amount: ₹{loan_amount:.2f}")

# !pip install flask flask-ngrok

from flask import Flask, request, render_template_string
import numpy as np
from flask_ngrok import run_with_ngrok
#
# Initialize Flask app
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app runs

# Dummy model (Replace with your trained model)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()  # Example, replace with your loaded model

# Loan eligibility calculation function
def predict_loan_amount(credit_score, annual_income, outstanding_debt):
    loan_multipliers = {"Good": 5, "Standard": 3, "Bad": 0}
    multiplier = loan_multipliers.get(credit_score, 0)
    max_loan = max(0, multiplier * annual_income - outstanding_debt)
    return max_loan

# HTML Templates
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Credit Score and Loan Prediction</title>
</head>
<body>
    <h1>Credit Score and Loan Prediction</h1>
    <form action="/predict" method="post">
        <label>Annual Income:</label><br>
        <input type="number" name="annual_income" required><br>
        <label>Monthly Inhand Salary:</label><br>
        <input type="number" name="monthly_salary" required><br>
        <label>Number of Bank Accounts:</label><br>
        <input type="number" name="bank_accounts" required><br>
        <label>Number of Credit Cards:</label><br>
        <input type="number" name="credit_cards" required><br>
        <label>Interest Rate:</label><br>
        <input type="number" name="interest_rate" required><br>
        <label>Number of Loans:</label><br>
        <input type="number" name="loans" required><br>
        <label>Average Days Delayed:</label><br>
        <input type="number" name="avg_delay" required><br>
        <label>Number of Delayed Payments:</label><br>
        <input type="number" name="delayed_payments" required><br>
        <label>Credit Mix (Bad: 0, Standard: 1, Good: 2):</label><br>
        <input type="number" name="credit_mix" required><br>
        <label>Outstanding Debt:</label><br>
        <input type="number" name="outstanding_debt" required><br>
        <label>Credit History Age:</label><br>
        <input type="number" name="credit_history_age" required><br>
        <label>Monthly Balance:</label><br>
        <input type="number" name="monthly_balance" required><br><br>
        <button type="submit">Predict</button>
    </form>
</body>
</html>
"""

RESULT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prediction Results</title>
</head>
<body>
    <h1>Prediction Results</h1>
    <p><strong>Predicted Credit Score:</strong> {{ credit_score }}</p>
    <p><strong>Eligible Loan Amount:</strong> ₹{{ loan_amount }}</p>
    <a href="/">Go Back</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values
    a = float(request.form['annual_income'])
    b = float(request.form['monthly_salary'])
    c = int(request.form['bank_accounts'])
    d = int(request.form['credit_cards'])
    e = float(request.form['interest_rate'])
    f = int(request.form['loans'])
    g = float(request.form['avg_delay'])
    h = int(request.form['delayed_payments'])
    i = int(request.form['credit_mix'])
    j = float(request.form['outstanding_debt'])
    k = float(request.form['credit_history_age'])
    l = float(request.form['monthly_balance'])

    # Predict Credit Score (using dummy logic; replace with your model)
    features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
    predicted_credit_score = "Good"  # Replace with model.predict(features)

    # Predict loan amount
    loan_amount = predict_loan_amount(predicted_credit_score, a, j)

    return render_template_string(RESULT_HTML, credit_score=predicted_credit_score, loan_amount=loan_amount)

# Run the app
app.run()