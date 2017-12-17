import Readers.All_Reader as ar
import os
import Config as config
import Plotting.BarPlots as bp

years = ['2012', '2013', '2014', '2015', '2016', 'Group']
directories = ['Deaths', 'Hard', 'Total']
dir = ['Age', 'Months', 'Practice']

def directory_structure():
    if not os.path.exists(config.PLOTS_PATH):
        os.makedirs(config.PLOTS_PATH)
        for actual_dir in dir:
            directory = config.PLOTS_PATH + "\\" + actual_dir
            os.makedirs(directory)
            for year in years:
                os.makedirs(directory + '\\' + year)
                if year == 'Group':
                    continue;
                for direc in directories:
                    os.makedirs(directory + '\\' + year + '\\' + direc)


dict = ar.get_all()
directory_structure()
#bp.months(dict['Miesiące'])
#bp.practice(dict['Staż pracy'])
#bp.age(dict['Wiek pracownika'])
bp.months_grouped(dict['Miesiące'])
bp.practice_grouped(dict['Staż pracy'])
bp.age_grouped(dict['Wiek pracownika'])
