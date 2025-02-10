import pandas as pd
from faker import Faker
import numpy as np

# Initialize Faker for Indian data
fake = Faker('en_IN')

# Function to generate Customer Demographics Dataset
def generate_customer_demographics(num_customers):
    data = []
    for _ in range(num_customers):
        customer = {
            "CustomerID": fake.unique.random_number(digits=6),
            "Name": fake.name(),
            "Age": np.random.randint(18, 70),
            "Gender": np.random.choice(["Male", "Female", "Other"]),
            "Occupation": np.random.choice(["Engineer", "Teacher", "Doctor", "Business", "Student", "Homemaker"]),
            "City": fake.city(),
            "State": fake.state(),
            "AccountOpenDate": fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
            "AccountType": np.random.choice(["Savings", "Current", "Fixed Deposit"]),
            "AverageBalance": round(np.random.uniform(1000, 500000), 2),
            "CreditScore": np.random.randint(300, 900),
            "IncomeRange": np.random.choice(["0-5L", "5-10L", "10-20L", "20L+"]),
        }
        data.append(customer)
    return pd.DataFrame(data)

# Function to generate Customer Transactions Dataset
def generate_customer_transactions(num_transactions, customer_ids):
    data = []
    for _ in range(num_transactions):
        transaction = {
            "TransactionID": fake.unique.random_number(digits=8),
            "CustomerID": np.random.choice(customer_ids),
            "TransactionDate": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            "TransactionTime": fake.time(),
            "Amount": round(np.random.uniform(100, 50000), 2),
            "TransactionType": np.random.choice(["Deposit", "Withdrawal", "Transfer"]),
            "TransactionChannel": np.random.choice(["ATM", "Online", "Branch"]),
            "BranchID": np.random.randint(1, 101),  # Assuming 100 branches
            "BalanceAfterTransaction": round(np.random.uniform(1000, 500000), 2),
        }
        data.append(transaction)
    return pd.DataFrame(data)

# Function to generate Loan Dataset
def generate_loan_data(num_loans, customer_ids):
    data = []
    for _ in range(num_loans):
        loan = {
            "LoanID": fake.unique.random_number(digits=6),
            "CustomerID": np.random.choice(customer_ids),
            "LoanAmount": round(np.random.uniform(50000, 5000000), 2),
            "InterestRate": round(np.random.uniform(8.0, 15.0), 2),
            "LoanStartDate": fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d'),
            "LoanEndDate": fake.date_between(start_date='today', end_date='+5y').strftime('%Y-%m-%d'),
            "LoanType": np.random.choice(["Personal", "Home", "Car", "Education"]),
            "EMIAmount": round(np.random.uniform(5000, 50000), 2),
            "EMIDueDate": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            "LoanStatus": np.random.choice(["Active", "Closed", "Defaulted"]),
            "DefaultFlag": np.random.choice(["Yes", "No"], p=[0.1, 0.9]),  # 10% default rate
        }
        data.append(loan)
    return pd.DataFrame(data)

# Function to generate Branch Performance Dataset
def generate_branch_performance(num_branches):
    data = []
    for _ in range(num_branches):
        branch = {
            "BranchID": fake.unique.random_number(digits=3),
            "BranchName": fake.company(),
            "City": fake.city(),
            "State": fake.state(),
            "TotalCustomers": np.random.randint(100, 10000),
            "TotalTransactions": np.random.randint(1000, 50000),
            "TotalLoanAmount": round(np.random.uniform(1000000, 50000000), 2),
            "TotalDeposits": round(np.random.uniform(500000, 20000000), 2),
            "BranchRevenue": round(np.random.uniform(100000, 10000000), 2),
            "BranchExpenses": round(np.random.uniform(50000, 5000000), 2),
        }
        data.append(branch)
    return pd.DataFrame(data)

# Function to generate Credit Card Transactions Dataset
def generate_credit_card_transactions(num_transactions, customer_ids):
    data = []
    for _ in range(num_transactions):
        transaction = {
            "TransactionID": fake.unique.random_number(digits=8),
            "CustomerID": np.random.choice(customer_ids),
            "TransactionDate": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            "TransactionAmount": round(np.random.uniform(100, 50000), 2),
            "MerchantCategory": np.random.choice(["Retail", "Dining", "Travel", "Groceries"]),
            "TransactionCity": fake.city(),
            "TransactionCountry": "India",
            "PaymentStatus": np.random.choice(["Success", "Failed"]),
            "CreditLimit": round(np.random.uniform(50000, 500000), 2),
            "AvailableCredit": round(np.random.uniform(1000, 500000), 2),
        }
        data.append(transaction)
    return pd.DataFrame(data)

# Function to generate Customer Feedback Dataset
def generate_customer_feedback(num_feedbacks, customer_ids):
    data = []
    for _ in range(num_feedbacks):
        feedback = {
            "FeedbackID": fake.unique.random_number(digits=6),
            "CustomerID": np.random.choice(customer_ids),
            "FeedbackDate": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            "FeedbackChannel": np.random.choice(["Online", "Branch", "Phone"]),
            "FeedbackCategory": np.random.choice(["Service", "Product", "Website"]),
            "FeedbackText": fake.sentence(),
            "SentimentScore": np.random.choice(["Positive", "Negative", "Neutral"]),
            "ResolutionStatus": np.random.choice(["Resolved", "Pending"]),
        }
        data.append(feedback)
    return pd.DataFrame(data)

# Function to generate Fraud Detection Dataset
def generate_fraud_detection_data(num_transactions, customer_ids):
    data = []
    for _ in range(num_transactions):
        transaction = {
            "TransactionID": fake.unique.random_number(digits=8),
            "CustomerID": np.random.choice(customer_ids),
            "TransactionDate": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            "TransactionAmount": round(np.random.uniform(100, 50000), 2),
            "TransactionType": np.random.choice(["Deposit", "Withdrawal", "Transfer"]),
            "TransactionLocation": fake.city(),
            "FraudFlag": np.random.choice(["Yes", "No"], p=[0.05, 0.95]),  # 5% fraud rate
        }
        data.append(transaction)
    return pd.DataFrame(data)

# Generate datasets
num_customers = 1000
num_transactions = 10000
num_loans = 500
num_branches = 100
num_feedbacks = 200
num_fraud_transactions = 1000

# Generate Customer Demographics
customer_df = generate_customer_demographics(num_customers)
customer_ids = customer_df["CustomerID"].tolist()

# Generate other datasets
transactions_df = generate_customer_transactions(num_transactions, customer_ids)
loan_df = generate_loan_data(num_loans, customer_ids)
branch_df = generate_branch_performance(num_branches)
credit_card_df = generate_credit_card_transactions(num_transactions, customer_ids)
feedback_df = generate_customer_feedback(num_feedbacks, customer_ids)
fraud_df = generate_fraud_detection_data(num_fraud_transactions, customer_ids)

# Save datasets to CSV files
customer_df.to_csv("customer_demographics.csv", index=False)
transactions_df.to_csv("customer_transactions.csv", index=False)
loan_df.to_csv("loan_data.csv", index=False)
branch_df.to_csv("branch_performance.csv", index=False)
credit_card_df.to_csv("credit_card_transactions.csv", index=False)
feedback_df.to_csv("customer_feedback.csv", index=False)
fraud_df.to_csv("fraud_detection.csv", index=False)

print("All datasets generated and saved as CSV files.")
