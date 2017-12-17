#Wiek pracownika
import Config as rc
import pandas as pd
import os
import numpy as np

key = 'Wiek pracownika'
sheet_name = "tabl.7"
column_names = ['A', 'Dziedzina', 'C', 'D', 'Ogółem', 'Poniżej 18', '18-19', '20-29', '30-39', '40-49', '50-54', '55-59', '60-64', '>64']

def parse_sheet(xl):
    df = pd.read_excel(xl, sheet_name, skiprows=10)
    df.columns = column_names
    df = df.drop('A', 1)
    df = df.drop('C', 1)
    df = df.drop('D', 1)
    df = df[pd.notnull(df['Ogółem'])]
    return df

def get_one(file_name):
     path = os.path.join(rc.DATA_PATH, file_name)
     xl = pd.ExcelFile(path)
     return parse_sheet(xl)

def read_xlsx(max_years=5):
    sheet_dict = dict()
    for file_index, file_name in enumerate(os.listdir(rc.DATA_PATH)):
        if file_index < max_years:
            df = get_one(file_name)
            sheet_dict[file_name[0:len(file_name)-4]] = df
    return sheet_dict
