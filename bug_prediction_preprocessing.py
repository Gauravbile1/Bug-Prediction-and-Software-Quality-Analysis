import pandas as pd
import os

# Define file paths
data_path = r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\project 3\github_data.csv"
preprocessed_data_path = r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\project 3\preprocessed_github_data.csv"  # Changed path

# Check if the directory exists, if not, create it
directory = os.path.dirname(preprocessed_data_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Read the original data
data = pd.read_csv(data_path)

# Show the original data shape and first few rows
print(f"Original data shape: {data.shape}")
print("Original data (first few rows):")
print(data.head())

# Check for missing values
print("Missing values per column:")
print(data.isnull().sum())

# Convert relevant columns to strings before filling NaN values
data['title'] = data['title'].astype(str).fillna('No Title Provided')
data['body'] = data['body'].astype(str).fillna('No Body Provided')
data['state'] = data['state'].astype(str).fillna('Unknown')

# Ensure the 'labels' and 'is_buggy' columns are correctly set (e.g., binary labels)
data['labels'] = data['labels'].fillna(-1)  # Assuming -1 indicates missing labels
data['is_buggy'] = data['is_buggy'].fillna(-1)  # Assuming -1 indicates missing buggy state

# Remove rows with missing 'message' column (if any)
data = data.dropna(subset=['message'])

# Verify the shape of the cleaned data
print(f"Preprocessed data shape: {data.shape}")
print("Preprocessed data (first few rows):")
print(data.head())

# Save the preprocessed data to a CSV file
data.to_csv(preprocessed_data_path, index=False)

# Print confirmation message (without the emoji to avoid UnicodeEncodeError)
print(f"Preprocessed data saved to {preprocessed_data_path}")
