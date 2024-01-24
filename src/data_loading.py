## Loading raw USA & Canada Pipeline incident data into dataframes (from csv files)

# imports
import pandas as pd
from pathlib import Path

## making file path imports more robust

# get directory of current file
current_script_directory = Path(__file__).parent

# Construct path to data files given relative location
cad_string = current_script_directory / "../data/raw/canada/"
usa_string = current_script_directory  / "../data/raw/usa/"

cad_data = cad_string / "pipeline-incidents-comprehensive-data.csv"
cad_unknown_data = cad_string / "PODSdb_MDOTW_VW_OCCURRENCE_PUBLIC.csv"

usa_pre1986 = usa_string / "accident_hazardous_liquid_pre1986/accident_hazardous_liquid_pre1986.txt"
usa_1986_jan2002 = usa_string / "accident_hazardous_liquid_1986_jan2002/accident_hazardous_liquid_1986_jan2002.txt"
usa_jan2002_dec2009 = usa_string / "accident_hazardous_liquid_jan2002_dec2009/accident_hazardous_liquid_jan2002_dec2009.txt"
usa_jan2010_present = usa_string / "accident_hazardous_liquid_jan2010_present/accident_hazardous_liquid_jan2010_present.txt"
usa_gravity = usa_string / "accident_gravity_reporting_regulated_jul2020_present/accident_gravity_reporting_regulated_jul2020_present.txt"

# Convert to string if necessary (e.g., for pandas read_csv)
## DOESNT SEEM TO BE NECESSARY - START USING IF RUNNING INTO ISSUES
#cad_data_file_path_str = str(cad_data_file_path.resolve())

# reads .csv files (from opencanada dataset) from filepath and converts to pandas dataframe
def read_csv_to_dataframe(filepath, delimiter=',', encoding='UTF-8'):
    try:
        df = pd.read_csv(filepath, delimiter=delimiter, encoding=encoding)
        print(f"File at '{filepath}' successfully read into a DataFrame.")
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

# reads .txt files (from PHMSA) from filepath and convers to pandas dataframe
# PHMAS mentions that: delimiter = Tab, text qualifier = {none} (quoting=3), and treat consecutive delimiters as one = off (default in read_csv)
def read_txt_to_dataframe(filepath, low_memory=False):
    try:
        df = pd.read_csv(filepath, delimiter='\t', quoting=3, low_memory=low_memory)
        print(f"TXT file at '{filepath}' successfully read into a DataFrame.")
        return df
    except Exception as e:
        print(f"Error reading the TXT file: {e}")
        return None

# read data into dataframes
CAD_data_raw = read_csv_to_dataframe(cad_data)
CAD_unknown_data_raw = read_csv_to_dataframe(cad_unknown_data)

usa_pre1986_raw = read_txt_to_dataframe(usa_pre1986)
usa_1986_jan2002_raw = read_txt_to_dataframe(usa_1986_jan2002)
usa_jan2002_dec2009_raw = read_txt_to_dataframe(usa_jan2002_dec2009)
usa_jan2010_present_raw = read_txt_to_dataframe(usa_jan2010_present)
usa_gravity_raw = read_txt_to_dataframe(usa_gravity)


