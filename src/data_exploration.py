import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    """
    Perform data exploration on the dataset.
    Args:
        df (pandas.DataFrame): The dataset to explore.

    Returns:
        None
    """
    print(df.info())
    print(df.describe())
    print(df['species'].value_counts())

    # Pairplot for data visualization
    sns.pairplot(df, hue='species', diag_kind='hist')
    plt.show()
