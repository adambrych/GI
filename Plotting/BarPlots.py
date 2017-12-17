import matplotlib.pyplot as plt
import Config as config
import numpy as np
import pandas as pd

def months(dict):
    x =['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    #plotting(dict, x, 'Months')
    plotting(dict, x, 'Months', 'Miesiąc')

def age(dict):
    x = ['Poniżej 18', '18-19', '20-29', '30-39', '40-49', '50-54', '55-59', '60-64', '>64']
    #plotting(dict, x, 'Age')
    plotting(dict, x, 'Age', 'Wiek')

def practice(dict):
    x = ['1', '2-3', '4-5', '6-10', '11-15', '16-20', '21-30', '>31']
    #plotting(dict,x, 'Practice')
    plotting(dict, x, 'Practice', 'Staż pracy')


def plotting(dict, x, dir, x_label):
    y_label = 'Liczba wypadków'
    title_A = 'Liczba wypadków ze względu na ' + x_label + ' w sektorze '
    title_B = 'Liczba wypadków śmiertelnych ze względu na ' + x_label + ' w sektorze '
    title_C = 'Liczba wypadków ciężkich ze względu na ' + x_label + ' w sektorze '
    for year in dict.keys():
        actualYearDataFrame = dict[year]
        actualYearDataFrame = actualYearDataFrame.reset_index(drop=True)
        for index, row in actualYearDataFrame.iterrows():
            if index > len(actualYearDataFrame)/2-1: # nie branie odsetek
                break
            y = []
            for arg in x:
                y.append(row[arg])
            x_number = range(0, len(x))
            fig = plt.figure()
            plt.bar(x_number, y)
            plt.xticks(x_number, x, rotation=45)
            plt.ylabel(y_label)
            plt.xlabel(x_label)
            if index%3 == 0:
                work = row['Dziedzina']
                title =  title_A + work + ' w roku ' + year
                path = year + '\\Total\\'

            elif index%3 == 1:
                title = title_B + work + ' w roku ' + year
                path = year + '\\Deaths\\'
            else:
                title = title_C + work + ' w roku ' + year
                path = year + '\\Hard\\'
            plt.title(title)
            title = title.replace(' ', '_')
            title = title.replace('.', '')
            title = title.replace('\n', '')
            title = year + '_' + title
            fig.savefig(config.PLOTS_PATH + '\\' + dir +'\\' + path + title, bbox_inches='tight', dpi=fig.dpi)
            plt.cla()
            plt.close()
            plt.clf()
            print(title)
            #print("x ", x)
            #print("y ", y)
            #plt.show()

def plotting_percent(dict, x, dir):
    y_label = 'Odsetek wypadków'
    title_A = 'Odsetek wypadków w sektorze '
    title_B = 'Odsetek wypadków śmiertelnych w sektorze '
    title_C = 'Odsetek wypadków ciężkich w sektorze '
    for year in dict.keys():
        actualYearDataFrame = dict[year]
        actualYearDataFrame = actualYearDataFrame.reset_index(drop=True)
        for index, row in actualYearDataFrame.iterrows():
            if index < len(actualYearDataFrame)/2: # nie branie calkowitych
                continue
            y = []
            for arg in x:
                y.append(row[arg])
            x_number = range(0, len(x))
            fig = plt.figure()
            plt.bar(x_number, y)
            plt.xticks(x_number, x, rotation=45)
            plt.ylabel(y_label)
            if index%3 == 0:
                work = row['Dziedzina']
                title =  title_A + work + ' w roku ' + year
                path = year + '\\Total\\'

            elif index%3 == 1:
                title = title_B + work + ' w roku ' + year
                path = year + '\\Deaths\\'
            else:
                title = title_C + work + ' w roku ' + year
                path = year + '\\Hard\\'
            plt.title(title)
            title = title.replace(' ', '_')
            title = title.replace('.', '')
            title = title.replace('\n', '')
            title = year + '_' + title
            fig.savefig(config.PLOTS_PATH + '\\' + dir +'\\' + path + title, bbox_inches='tight', dpi=fig.dpi)
            plt.cla()
            plt.close()
            plt.clf()
            #print(title)
            #print("x ", x)
            #print("y ", y)
            #plt.show()

def months_grouped(dict):
    x =['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    plotting_grouped(dict, x, 'Months', 2, 'Miesiąc')

def age_grouped(dict):
    x = ['Poniżej 18', '18-19', '20-29', '30-39', '40-49', '50-54', '55-59', '60-64', '>64']
    plotting_grouped(dict, x, 'Age', 1, 'Wiek')

def practice_grouped(dict):
    x = ['1', '2-3', '4-5', '6-10', '11-15', '16-20', '21-30', '>31']
    plotting_grouped(dict, x, 'Practice', 1, 'Staż Pracy')

def plotting_grouped(dict, x,dir, w, x_label):
    y_label = 'Liczba wypadków'
    title_A = 'Liczba wypadków ze względu na ' + x_label + ' w sektorze '
    title_B = 'Liczba wypadków śmiertelnych ze względu na ' + x_label + ' w sektorze '
    title_C = 'Liczba wypadków ciężkich ze względu na ' + x_label + ' w sektorze '
    for year in dict.keys():
        dict[year] = dict[year].reset_index(drop=True)
    for index in range(0, len(dict[list(dict.keys())[0]].index)):
        if index > len(dict[list(dict.keys())[0]].index)/2-1: # nie branie odsetek
                break
        y = []
        y_index = 0
        for year in dict.keys():
            y.append([])

            for i in range(0, len(x)):
                y[y_index].append(dict[year].iloc[[index]][x[i]].values[0])
            y_index += 1

        if index % 3 == 0:
            work = dict[year].iloc[[index]]['Dziedzina'].values[0]
            title = title_A + work
        elif index % 3 == 1:
            title = title_B + work
        else:
            title = title_C + work


        dim = len(y[0])
        dimw = w / dim
        fig = plt.figure()
        x_plot = np.arange(len(x))
        for i in range(0,len(y)):
            plt.bar(x_plot + i * dimw, pd.to_numeric(y[i]), dimw)

        plt.xticks(x_plot, x, rotation=45)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        plt.legend(['2012', '2013', '2014', '2015', '2016'])
        title = title.replace(' ', '_')
        title = title.replace('.', '')
        title = title.replace('\n', '')
        fig.savefig(config.PLOTS_PATH + '\\' + dir + '\\Group\\' + title, bbox_inches='tight', dpi=fig.dpi)

        plt.cla()
        plt.close()
        plt.clf()