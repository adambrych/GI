#Staż pracy
import Config as rc
import pandas as pd
import os
import numpy as np

key = 'Staż pracy'
sheet_name = "tabl.8 "
column_names = ['A', 'Dziedzina', 'C', 'D', 'Ogółem', '1', '2-3', '4-5', '6-10', '11-15', '16-20', '21-30', '>31']

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
