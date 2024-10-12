import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_clean_data(file_path):
    """
    Load and preprocess the dataset.
    Adjust column names based on the dataset structure.
    """
    df = pd.read_csv(file_path)

    # Handle missing values (if any)
    df.dropna(inplace=True)

    # Perform any encoding or adjustments (replace 'Class/ASD' with your actual target column)
    df = pd.get_dummies(df, drop_first=True)

    return df


def split_data(df, target_column):
    """
    Split data into training and test sets.
    """
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)
