# DATA PROCESSING USING AI
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from google.colab import files

# Step 1: Upload the dataset (Manually upload the dataset file)
print("Please upload your dataset file (.csv) using the button below.")
uploaded = files.upload()

# Once uploaded, we get the filename from the 'uploaded' dictionary
filename = next(iter(uploaded))

# Step 2: Load the dataset into a pandas DataFrame
data = pd.read_csv(filename)

# Print dataset overview
print("Dataset Overview:")
print(data.head())
print("Dataset Columns:", data.columns)

# Step 3: Handle Missing Values
# Impute numerical columns with the mean
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
print(f"Numerical Columns to Impute: {numerical_columns}")
imputer = SimpleImputer(strategy='mean')
data[numerical_columns] = imputer.fit_transform(data[numerical_columns])

# Impute categorical columns with the most frequent value (mode)
categorical_columns = data.select_dtypes(include=['object']).columns
print(f"Categorical Columns to Impute: {categorical_columns}")
imputer_cat = SimpleImputer(strategy='most_frequent')
data[categorical_columns] = imputer_cat.fit_transform(data[categorical_columns])

# Step 4: Encode Categorical Variables using One-Hot Encoding
print("Performing One-Hot Encoding on Categorical Variables...")
data = pd.get_dummies(data, drop_first=True)

# Check the dataset after One-Hot Encoding
print("Data after One-Hot Encoding:")
print(data.head())

# Step 5: Scale Features
print("Scaling Numerical Features...")
scaler = StandardScaler()
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Step 6: Split Data into Features and Target
# Replace 'target_column' with the actual name of your target column
target_column = 'Target'  # Replace with actual target column name
X = data.drop(target_column, axis=1)  # Features (everything except the target column)
y = data[target_column]  # Target

# Check the shape of X and y to ensure they match
print(f"Features (X) shape: {X.shape}, Target (y) shape: {y.shape}")

# Step 7: Split the data into training and testing sets
# Remove 'stratify=y' to avoid the error
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Final confirmation
print("Data processing complete!")
print(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
