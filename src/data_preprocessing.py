from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    """
    Preprocess the dataset by converting categorical variables and splitting it into training and testing sets.
    Args:
        df (pandas.DataFrame): The dataset to preprocess.

    Returns:
        tuple: A tuple containing X_train, X_test, y_train, y_test.
    """
    label_encoder = LabelEncoder()
    df['species'] = label_encoder.fit_transform(df['species'])

    X = df.drop('species', axis=1)
    y = df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
