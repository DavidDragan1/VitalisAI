import pandas as pd

# load .csv
def load_csv(file_path):
    return pd.read_csv(file_path)

# preprocess the DataFrame
def preprocess_data(df):
    # remove entries with missing values in the "Symptom Description" column
    df.dropna(subset=["Symptom Description"], inplace=True)

    # remove the "Insurance Status" column as irrelevant
    df.drop(columns=["Insurance Status"], inplace=True, errors='ignore')  # Use errors='ignore' to avoid KeyError if the column doesn't exist

    return df

# convert DataFrame to JSON array format
def convert_to_json(df, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json_data = df.to_json(orient='records', lines=False)
        json_file.write(json_data)

# main function to run the steps
def main(csv_file_path, json_file_path):
    df = load_csv(csv_file_path)
    print("Original DataFrame:")
    print(df)

    cleaned_df = preprocess_data(df)
    print("\nCleaned DataFrame:")
    print(cleaned_df)

    convert_to_json(cleaned_df, json_file_path)
    print(f"\nData successfully converted to JSON and saved to {json_file_path}")

if __name__ == "__main__":
    csv_file = 'data/raw_dataset.csv'
    json_file = 'data/data_preprocessed.json'  # .json output path
    main(csv_file, json_file)
