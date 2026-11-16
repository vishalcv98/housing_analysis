import pandas as pd

def load_dataframes(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None

def combine_dataframes(df_a, df_b, df_c, df_d):
    """
    Combine four DataFrames into a single DataFrame.

    Parameters:
    df_a, df_b, df_c, df_d (pd.DataFrame): The DataFrames to combine.

    Returns:
    pd.DataFrame: A combined DataFrame.
    """
    part_a = pd.concat([df_a, df_c], ignore_index=True)
    part_b = pd.concat([df_b, df_d], ignore_index=True)
    combined_df = pd.merge(part_a, part_b, on="Id")
    return combined_df
    