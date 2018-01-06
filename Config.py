import os
import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = ROOT_DIR + '\\Data'
PLOTS_PATH = ROOT_DIR + '\\Plots'
IMG_PATH = ROOT_DIR + '\\Img'
MAP_PATH = ROOT_DIR + '\\Maps'
YEAR_ARG = "--year"
YEAR_ARG_DEFAULT = datetime.datetime.now().year - 1
YEAR_ARG_USER = None
