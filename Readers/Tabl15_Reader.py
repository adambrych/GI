#Umiejscowienie urazów
import Config as rc
import pandas as pd
import os
import numpy as np

key = 'Umiejscowienie urazów'
sheet_name = "tabl.15 "
column_names = ['A', 'Dziedzina', 'C', 'D', 'Ogółem', 'Głowa', 'Szyja wraz z kręgosłupem szyjnym', 'Grzbiet łącznie z kręgosłupem', 'Tułów i organy wewnętrzne', 'Kończyny górne', 'Kończyny dolne', 'Całe ciało i jego różne części']

def parse_sheet(xl):
    df = pd.read_excel(xl, sheet_name, skiprows=7)
    df.columns = column_names
    df = df.drop('A', 1)
    df = df.drop('C', 1)
    df = df.drop('D', 1)
    df = df[np.isfinite(df['Ogółem'])]
    return df

def get_one(file_name):
     path = os.path.join(rc.DATA_PATH, file_name)
     xl = pd.ExcelFile(path)
     return parse_sheet(xl)

def read_xlsx(max_years=4):
    sheet_dict = dict()
    for file_index, file_name in enumerate(os.listdir(rc.DATA_PATH)):
        if file_index < max_years:
            df = get_one(file_name)
            sheet_dict[file_name[0:len(file_name)-4]] = df
    return sheet_dict