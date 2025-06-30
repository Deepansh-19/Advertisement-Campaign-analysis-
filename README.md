Advertisement Campaign Analysis
This project analyzes a bank marketing dataset to uncover insights about customer demographics, campaign outcomes, and potential indicators of success in telemarketing campaigns.

It was developed as part of the Finlatics Financial Analytics Virtual Experience Program.

Dataset
The dataset used is named banking_data.csv and contains client information from a bank's marketing campaign. Each row represents a customer, along with data such as:

Personal attributes (age, job, marital status, education)

Credit and balance information

Loan status

Contact history

Response to marketing campaigns

Objective
The goal of this project is to explore and visualize the data to:

Understand customer demographics

Analyze the effectiveness of past marketing efforts

Study the correlation of features with the campaign outcome

Assist in designing more targeted and successful advertisement campaigns

Tools Used:
Python

pandas – Data cleaning and manipulation

matplotlib & seaborn – Data visualization

NumPy – Numerical computations

Key Analyses :
Data Cleaning
Handled missing values in marital and education

Converted y (target variable) to binary format (Success or Failure)

📊 Exploratory Data Analysis
Distribution plots of categorical features like:

Marital status

Education

Housing and personal loans

Contact methods

Month and duration of last contact

Campaign Performance Metrics:

Number of contacts made

Days since last contact

Previous campaign outcomes

Correlation Analysis:

Created heatmaps to visualize correlation between numerical variables

Highlighted strong correlations with the campaign result (y_numeric)

Visualized top variable pairs with high correlation coefficients

Sample Visuals :

Bar plots of categorical variable distributions

Correlation heatmaps for numeric features

Bar plots showing strongest variable pair correlations

Insights : 

Some variables like duration of last contact and previous outcomes are strongly correlated with campaign success

Education and marital status showed varied patterns across successful and unsuccessful responses

