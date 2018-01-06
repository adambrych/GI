import argparse
import datetime
import Config
import Plotting.Human_Heatmap as Human_Heatmap

parser = argparse.ArgumentParser()

parser.add_argument(Config.YEAR_ARG, help='Zawezenie raportu do konkretnego roku')

args = parser.parse_args()
year = args.year
if year is not None:
    year = int(year)
    if year < 2000 or year >= datetime.datetime.now().year:
        year = Config.YEAR_ARG_DEFAULT
Config.YEAR_ARG_USER = year
Human_Heatmap.generate_heatmap()

