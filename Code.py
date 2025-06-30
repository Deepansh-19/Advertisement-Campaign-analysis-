from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reset pandas options
reset_option('display.max_rows')

# Load dataset
file_path = '/Users/deepansh/Desktop/Competitive Programming/Python files/banking_data.csv'
df = read_csv(file_path)

# Check for missing values
print(df.isnull().sum())

# --- Analysing Marital Status ---
marital_status_info = df['marital'].value_counts()
marital_status_info.plot(kind='bar')
plt.title("Marital Status Distribution")
plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.show()

# Drop rows with missing marital status
df.dropna(subset=['marital'], inplace=True)

# --- Analysing Education Qualification ---
print(df.isnull().sum())
education_status_info = df['education'].value_counts()
education_status_info.plot(kind='bar')
plt.title("Education Level Distribution")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.show()

# Drop rows with missing education
df.dropna(subset=['education'], inplace=True)

# --- Basic Column Info ---
print(df.isnull().sum())
print(df.columns)

# --- Age Distribution ---
age_distribution = df['age'].value_counts()
print(age_distribution)

# --- Job Type ---
job_type = df['job'].value_counts()
print(job_type)

# --- Marital Status ---
marital_status = df['marital'].value_counts()
print("Marital status of the clients is as follows:\n", marital_status)

# --- Education ---
education_qualification = df['education'].value_counts()
print(education_qualification)

# --- Credit Default ---
credit = df['default'].value_counts()
print(credit)

# --- Account Balance ---
balance_clients = df['balance'].value_counts()
print(balance_clients)

# --- Housing Loan ---
housing_loan = df['housing'].value_counts()
print(housing_loan)

# --- Personal Loan ---
personal_loan = df['loan'].value_counts()
print(personal_loan)

# --- Contact Method ---
communication_ways = df['contact'].value_counts()
print(communication_ways)

# --- Last Contact Day ---
last_contact_day = df['day'].value_counts()
print(last_contact_day)

# --- Last Contact Month ---
last_contact_month = df['month'].value_counts()
print(last_contact_month)

# --- Last Contact Duration ---
last_contact_duration = df['duration'].value_counts()
print(last_contact_duration)

# --- Number of Contacts During Campaign ---
campaign = df['campaign'].value_counts()
print(campaign)

# --- Days Since Last Contact ---
df['pdays'].replace({-1: 'Never contacted before'}, inplace=True)
days_passed = df['pdays'].value_counts()
print(days_passed)

# --- Previous Contacts ---
contacts_previously_performed = df['previous'].value_counts()
print(contacts_previously_performed)

# --- Previous Marketing Outcomes ---
previous_marketing_outcomes = df['poutcome'].value_counts()
print(previous_marketing_outcomes)

# --- Result of the Campaign ---
df['y'].replace({'yes': 'Success', 'no': 'Failure'}, inplace=True)
result = df['y'].value_counts()
print(result)

# --- Add binary target for correlation ---
df['y_numeric'] = df['y'].apply(lambda x: 1 if x == 'Success' else 0)

# --- Correlation with target variable ---
numeric_df = df.select_dtypes(include=['int64', 'float64']).copy()
numeric_df['y_numeric'] = df['y_numeric']

corr_matrix = numeric_df.corr()
corr_with_target = corr_matrix['y_numeric'].drop('y_numeric')

plt.figure(figsize=(10, 8))
sns.heatmap(corr_with_target.to_frame(), annot=True, cmap='coolwarm', fmt=".2f", cbar=False)
plt.title("Correlation with Success of Getting a New Client")
plt.xlabel("Features")
plt.ylabel("Correlation Coefficient")
plt.show()

# --- Full Correlation Matrix ---
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", annot_kws={"size": 10}, cbar_kws={"shrink": 0.8})
plt.title("Correlation Matrix of Numeric Features")
plt.show()

# --- Bar Graph for Pairwise Correlations ---
corr_pairs = corr_matrix.unstack().reset_index()
corr_pairs.columns = ['Variable1', 'Variable2', 'Correlation']

# Remove duplicates and self-correlations
corr_pairs = corr_pairs[corr_pairs['Variable1'] < corr_pairs['Variable2']]
corr_pairs = corr_pairs.sort_values(by='Correlation', ascending=False)

plt.figure(figsize=(14, 10))
sns.barplot(x='Correlation', y='Variable1', hue='Variable2', data=corr_pairs, dodge=False)
plt.title('Top Correlations Between Variable Pairs')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Variable Pairs')
plt.legend(title='Variable2', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
