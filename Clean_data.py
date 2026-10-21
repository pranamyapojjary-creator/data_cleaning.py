import pandas as pd
import os

# Load the original dataset
input_file = "sample_data.csv"

if os.path.exists(input_file):
    df = pd.read_csv(input_file)

    print("Original Dataset:")
    print(df.head())

    # Display missing values before cleaning
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(df[column].mean())

    # Save the cleaned dataset
    df.to_csv("cleaned_data.csv", index=False)

    print("\nData cleaning completed successfully!")
    print("Cleaned dataset saved as cleaned_data.csv")
    print("Total records after cleaning:", len(df))

else:
    print("Error: sample_data.csv not found.")
    print("Please add the original dataset to the project folder.")
