import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import warnings

# Prompting the user for the path to the CSV file
csv_path = input("Enter the path to your CSV file: ")

# Importing the dataset
dataset = pd.read_csv(csv_path)

while True:
    # Extracting the relevant columns
    columns_to_impute = input("Enter the columns you want to impute (separated by commas): ").split(',')

    # Check if columns contain numerical values
    non_numeric_columns = [col for col in columns_to_impute if not pd.to_numeric(dataset[col], errors='coerce').notnull().all()]
    if non_numeric_columns:
        warnings.warn("The following columns contain non-numeric values: {}".format(", ".join(non_numeric_columns)))
        continue  # Ask the user to re-enter the columns

    # Proceed with imputation only if all selected columns contain numerical values
    else:
        # Find indices where values are 0
        missing_mask = dataset[columns_to_impute] == 0

        # Handling missing data
        imputer = SimpleImputer(missing_values=0, strategy='median')  # Strategy set to 'median' as default, since we'll handle zeros manually
        X_imputed = imputer.fit_transform(dataset[columns_to_impute])

        # Introducing variance
        variance = np.random.uniform(low=-0.2, high=0.2, size=X_imputed.shape)
        X_imputed_with_variance = X_imputed * (1 + variance)

        # Apply imputed values only where the original values were 0
        X_imputed_with_variance = np.where(missing_mask, X_imputed_with_variance, dataset[columns_to_impute])

        # Round the imputed values to the nearest integer
        X_imputed_with_variance_rounded = np.round(X_imputed_with_variance)

        # Update the DataFrame with the rounded imputed values
        dataset[columns_to_impute] = X_imputed_with_variance_rounded

        # Get the directory of the original CSV file
        output_directory = os.path.dirname(csv_path)

        # Generate the path for the new CSV file
        new_csv_path = os.path.join(output_directory, "imputed_" + os.path.basename(csv_path))

        # Write the updated DataFrame back to the CSV file
        dataset.to_csv(new_csv_path, index=False)

        print("Imputed data with variance (rounded to nearest zero) saved to '{}'.".format(new_csv_path))
        break  # Exit the loop once valid columns are provided
