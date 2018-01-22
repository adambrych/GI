import Readers.Map_Reader as Map_Reader
import Readers.Tabl33_Reader as District_Reader
import pandas as pd
import matplotlib.pyplot as plt


def generate_map():
    poland = Map_Reader.read_map()
    poland.scale(xfact=0.7)
    poland = poland.sort_values(by="name", ascending=True)
    data = District_Reader.read_xlsx()
    title = "2016"
    year = data[title]
    year = year.drop([0])
    year = year.sort_values(by=year.columns[0], ascending=True)
    year_list = year[year.columns[2]].tolist()
    poland['plot'] = pd.Series(year_list, index=poland.index)
    poland.plot(column='plot', scheme='fisher_jenks', cmap='Reds', legend=True)
    ax = plt.gca()
    leg = ax.get_legend()
    leg.set_bbox_to_anchor((0.5, -0.2, 0.0, 0.0))

    plt.axis('off')
    plt.title("Kwota wyplaconych odszkodowan w roku " + title)
    plt.savefig("odszkodowania_kwota_"+title+".png", bbox_inches='tight')
    plt.close()

# generate_map()
