from sklearn.cluster import KMeans
import pandas as pd

def add_missing_columns(data):
    """
    Add missing columns with default values to ensure that the data has all required columns.
    """
    required_columns = ['age', 'income', 'gender_male', 'gender_female']
    for col in required_columns:
        if col not in data.columns:
            # Add missing column with default value
            if col in ['gender_male', 'gender_female']:
                # Assuming gender columns should be binary, default to 0
                data[col] = 0
            else:
                # Assuming numeric columns, default to 0
                data[col] = 0
    return data

def demographic_segmentation(data, n_clusters=4):
    """
    Perform demographic segmentation using KMeans clustering.
    """
    data = add_missing_columns(data)
    
    demographic_data = data[['age', 'income', 'gender_male', 'gender_female']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['demographic_segment'] = kmeans.fit_predict(demographic_data)
    return data

# Example usage
if __name__ == "__main__":
    filepaths = [
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Brand_Lover.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Camera_Lover.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Customer-Data.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Dataset.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\name.csv',
        r'C:\Users\admin\Desktop\Test Project\project\data\datasets\Products.csv',
    ]

    for filepath in filepaths:
        try:
            data = pd.read_csv(filepath)
            print(f"Processing file: {filepath}")
            segmented_data = demographic_segmentation(data)
            print(f"Segmented data from {filepath}:")
            print(segmented_data.head())
        except Exception as e:
            print(f"Error processing file {filepath}: {e}")
