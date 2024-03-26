Imputation Tool for Handling Missing Data
Overview:

This Python script provides a simple yet effective solution for handling missing data in a dataset. It utilizes the scikit-learn library to impute missing values using various strategies such as median, mean, etc.

Features:

    Reads data from a CSV file.
    Allows the user to specify columns containing missing values.
    Imputes missing values using the specified strategy.
    Saves the imputed dataset back to a CSV file.

Dependencies:

    Python 3.x
    NumPy
    pandas
    scikit-learn

Usage:

    git clone https://github.com/Lucas-Jeanniot/Database_Variance_Imputer.git

 

Install Dependencies:

````
pip install numpy pandas scikit-learn
`````
Run the Script:
````
   1. python Dataset_Imputation.py

   2. Input:
      - CSV path you want to impute data on
      - Columns you want to impute
      
  

    Output:
    The script will generate a new CSV file with imputed values, saving it in the same directory as the original file.
````
Example:

Suppose you have a CSV file named data.csv with missing values in columns A, B, and C. You can use this script to impute missing values using the median strategy and save the updated dataset to a new file named imputed_data.csv.



# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Importing the dataset
dataset = pd.read_csv('data.csv')

# Extracting the relevant columns
X = dataset[['A', 'B', 'C']]

# Handling missing data
imputer = SimpleImputer(missing_values=0, strategy='median')
X_imputed = imputer.fit_transform(X)

# Update the DataFrame with the imputed values
dataset[['A', 'B', 'C']] = X_imputed

# Write the updated DataFrame back to the CSV file
dataset.to_csv('imputed_data.csv', index=False)

print("Imputed data saved to 'imputed_data.csv'.")

