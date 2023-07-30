import pandas as pd

def load_dataset(file_path):
    """
    Load the dataset from the specified file path.
    Args:
        file_path (str): Path to the dataset file (e.g., CSV).

    Returns:
        pandas.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)
