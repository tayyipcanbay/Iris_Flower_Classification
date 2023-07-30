from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    """
    Train the logistic regression model on the training data.
    Args:
        X_train (pandas.DataFrame): Training features.
        y_train (pandas.Series): Training labels.

    Returns:
        sklearn.linear_model.LogisticRegression: The trained logistic regression model.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model
