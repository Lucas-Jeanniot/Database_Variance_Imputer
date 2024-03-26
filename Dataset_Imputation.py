import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Prompting the user for the path to the CSV file
csv_path = input("Enter the path to your CSV file: ")

# Importing the dataset
dataset = pd.read_csv(csv_path)

# Extracting the relevant columns
columns_to_impute = input("Enter the columns you want to impute (separated by commas): ").split(',')
X = dataset[columns_to_impute]

# Handling missing data
imputer = SimpleImputer(missing_values=0, strategy='median')  # <-- Change this to median, mean, etc depending on your dataset requirements
X_imputed = imputer.fit_transform(X)

# Introducing variance
variance = np.random.uniform(low=-0.2, high=0.2, size=X_imputed.shape)
X_imputed_with_variance = X_imputed * (1 + variance)

# Update the DataFrame with the imputed values
for i, col in enumerate(columns_to_impute):
    dataset[col] = X_imputed_with_variance[:, i]

# Get the directory of the original CSV file
output_directory = os.path.dirname(csv_path)

# Generate the path for the new CSV file
new_csv_path = os.path.join(output_directory, "imputed_with_variance_" + os.path.basename(csv_path))

# Write the updated DataFrame back to the CSV file
dataset.to_csv(new_csv_path, index=False)

print("Imputed data with variance saved to '{}'.".format(new_csv_path))
