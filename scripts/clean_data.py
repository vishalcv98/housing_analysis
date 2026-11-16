import pandas as pd
import numpy as np

def replace_with_na(df,columns):
    """
    Replace missing values in specified columns with 'N/A'.

    Parameters:
    columns (list): A list of column names to process.

    Returns:
    None
    """
    for column in columns:
        if column in df.columns:
            df[column].fillna('N/A', inplace=True)
        else:
            print(f"Warning: Column '{column}' does not exist in the DataFrame.")

    return df

def replace_nulls_with_median(df,columns):
    """
    Replace missing values in specified columns with the median of that column.

    Parameters:
    columns (list): A list of column names to process.

    Returns:
    None
    """
    for column in columns:
        if column in df.columns:
            median_value = df[column].median()
            df[column].fillna(median_value, inplace=True)
        else:
            print(f"Warning: Column '{column}' does not exist in the DataFrame.")
    return df


def drop_duplicates(df, columns):
    """
    Drop duplicate rows from the DataFrame.

    Returns:
    None
    """
    df.drop_duplicates(subset=columns, inplace=True)
    return df

