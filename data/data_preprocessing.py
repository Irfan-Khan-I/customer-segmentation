import sys
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_collection import load_data, load_multiple_data, combine_data

def preprocess_data(data):
    """
    Perform preprocessing on the DataFrame.
    - Handle missing values
    - Encode categorical features
    - Normalize numerical features
    """
    # Handle missing values
    data = data.fillna(method='ffill')

    # Separate features
    categorical_features = data.select_dtypes(include=['object']).columns
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns

    # Encode categorical features if there are any
    if categorical_features.size > 0:
        encoder = OneHotEncoder(drop='first', sparse_output=False)  # Updated argument
        encoded_categorical_data = encoder.fit_transform(data[categorical_features])
        encoded_categorical_df = pd.DataFrame(encoded_categorical_data, columns=encoder.get_feature_names_out(categorical_features))
    else:
        encoded_categorical_df = pd.DataFrame()  # Empty DataFrame if no categorical features

    # Normalize numerical features if there are any
    if numerical_features.size > 0:
        scaler = StandardScaler()
        scaled_numerical_data = scaler.fit_transform(data[numerical_features])
        scaled_numerical_df = pd.DataFrame(scaled_numerical_data, columns=numerical_features)
    else:
        scaled_numerical_df = pd.DataFrame()  # Empty DataFrame if no numerical features

    # Combine all features
    processed_data = pd.concat(
        [scaled_numerical_df, encoded_categorical_df],
        axis=1
    )

    return processed_data
