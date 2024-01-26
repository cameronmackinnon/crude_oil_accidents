### OVERVIEW
# Functions to load raw USA & Canada Pipeline incident data into dataframes (from .csv or .txt files)

# imports
import pandas as pd

"""
Clean column headers:
- force column headers to be strings
- strip trailing spaces & replace multiple spaces with single space for column headers
"""
def clean_column_names(df):
    df.columns = [str(i).lower() for i in df.columns.values.tolist()] # force string and make lowercase
    df.columns = df.columns.str.strip()  # Remove leading and trailing spaces
    df.columns = df.columns.str.replace('  ', ' ') # Replace multiple spaces with a single space
    #df.columns = df.columns.map(lambda x: re ('\s+', ' ', regex=True))
    return df

"""
Read CSV to dataframe
- reads .csv files (from opencanada dataset) from filepath and converts to pandas dataframe
"""
def read_csv_to_dataframe(filepath, delimiter=',', encoding='UTF-8'):
    try:
        df = pd.read_csv(filepath, delimiter=delimiter, encoding=encoding)
        df = clean_column_names(df)
        print(f"File at '{filepath}' successfully read into a DataFrame.")
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

"""
Read .txt to dataframe
- reads .txt files (from PHMSA) from filepath and converts to pandas dataframe
- PHMAS mentions that: delimiter = Tab, text qualifier = {none} (quoting=3), and treat consecutive delimiters as one = off (default in read_csv)
"""
def read_txt_to_dataframe(filepath, low_memory=False):
    try:
        df = pd.read_csv(filepath, delimiter='\t', quoting=3, low_memory=low_memory)
        df = clean_column_names(df)
        print(f".txt file at '{filepath}' successfully read into a DataFrame.")
        return df
    except Exception as e:
        print(f"Error reading the .txt file: {e}")
        return None