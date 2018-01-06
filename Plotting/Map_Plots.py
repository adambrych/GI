import Readers.Map_Reader as Map_Reader
import Readers.Tabl33_Reader as District_Reader
import pandas as pd
import matplotlib.pyplot as plt


def generate_map():
    poland = Map_Reader.read_map()
    poland = poland.sort_values(by="name", ascending=True)
    data = District_Reader.read_xlsx()
    year = data["2009"]
    year = year.drop([0])
    year = year.sort_values(by=year.columns[0], ascending=True)
    year_list = year[year.columns[1]].tolist()
    poland['plot'] = pd.Series(year_list, index=poland.index)
    poland.plot(column='plot', scheme='fisher_jenks', cmap='Reds', k=16)
    plt.axis('off')
    plt.title("Liczba wyplaconych odszkodowan w roku 2013")
    plt.show()

generate_map()
