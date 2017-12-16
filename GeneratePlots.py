import Readers.All_Reader as ar
import os
import Config as config
import Plotting.BarPlots as bp

years = ['2013', '2014', '2015', '2016']
directories = ['Deaths', 'Hard', 'Total']

def directory_structure(dir, directories):
    directory = config.PLOTS_PATH + "\\" + dir
    if not os.path.exists(directory):
        os.makedirs(directory)
        for year in years:
            os.makedirs(directory + '\\' + year)
            for direc in directories:
                os.makedirs(directory + '\\' + year + '\\' + direc)


dict = ar.get_all()
#directory_structure('Months', directories)
#directory_structure('Months_percent', directories)
bp.months(dict['Miesiące'])
#directory_structure('Practice', directories)
#directory_structure('Practice_percent', directories)
bp.practice(dict['Staż pracy'])
#directory_structure('Age', directories)
#directory_structure('Age_percent', directories)
bp.age(dict['Wiek pracownika'])
bp.months_grouped(dict['Miesiące'])
bp.practice_grouped(dict['Staż pracy'])
bp.age_grouped(dict['Wiek pracownika'])
