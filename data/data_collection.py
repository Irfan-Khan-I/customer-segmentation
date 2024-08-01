import pandas as pd
import os

def load_data(filepath):
    """
    Load a CSV file into a pandas DataFrame.

    Args:
    - filepath (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded data as a DataFrame.
    """
    data = pd.read_csv(filepath)
    return data

def load_multiple_data(filepaths):
    """
    Load multiple CSV files into a list of DataFrames.

    Args:
    - filepaths (list): A list of file paths to the CSV files.

    Returns:
    - list: A list of pandas DataFrames, each corresponding to a CSV file.
    """
    dataframes = []
    for filepath in filepaths:
        try:
            df = load_data(filepath)
            dataframes.append(df)
        except Exception as e:
            print(f"Failed to load {filepath}: {e}")
    return dataframes

def combine_data(dataframes):
    """
    Combine multiple DataFrames into a single DataFrame.

    Args:
    - dataframes (list): A list of pandas DataFrames.

    Returns:
    - pd.DataFrame: A single DataFrame containing all the data.
    """
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

if __name__ == "__main__":
    # Define the file paths to the CSV files
    filepaths = [
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Brand_Lover.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Camera_Lover.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Customer-Data.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Dataset.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\name.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Products.csv',
    ]

    # Load the data from all files
    dataframes = load_multiple_data(filepaths)

    # Combine all data into a single DataFrame
    combined_data = combine_data(dataframes)

    # Display the first few rows of the combined DataFrame
    print(combined_data.head())
