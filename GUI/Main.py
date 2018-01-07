import tkinter as tk
from tkinter import ttk
import Config
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import Generate_Pdf


def generate_grid(year_from, year_to, filename, cols=3):
    if year_from == year_to:
        heatmap = mpimg.imread(Config.IMG_PATH + "\\" + filename + year_from + ".png")
        plt.imshow(heatmap)
    else:
        plt.figure(figsize=(15, 15))
        size = int(year_to) - int(year_from) + 1
        imgs = []
        for i in range(0, size):
            imgs.append(mpimg.imread(Config.IMG_PATH + "\\" + filename + str(int(year_from)+i) + ".png"))
        n_rows = (size // cols)
        if size % cols != 0:
            n_rows += 1
        n_cols = cols
        if size < cols:
            n_cols = size
        for i in range(0, size):
            plt.axis('off')
            plt.subplots_adjust(hspace =.001, wspace=.001)
            plt.subplot(n_rows, n_cols, i+1)
            plt.imshow(imgs[i])
    plt.axis('off')
    plt.savefig(Config.IMG_PATH + "\\" + filename+"grid.png", bbox_inches='tight')


def generate_grid_bar(year_from, year_to, sector, type, accident_type):
    cols = 2
    size = int(year_to) - int(year_from) + 1
    imgs = []
    for i in range(0, size):
        year = str(int(year_from)+i)
        imgs.append(mpimg.imread(Config.PLOTS_PATH + "\\" + type + "\\" + year + "\\" + accident_type + "\\" + sector + ".png"))
    n_rows = (size // cols)
    if size % cols != 0:
        n_rows += 1
    n_cols = cols
    if size < cols:
        n_cols = size
    for i in range(0, size):
        plt.axis('off')
        plt.subplots_adjust(hspace =.001, wspace=.001)
        plt.subplot(n_rows, n_cols, i+1)
        plt.imshow(imgs[i])
    plt.axis('off')
    plt.savefig(Config.IMG_PATH + "\\" + sector+"_"+type+"_"+accident_type+"_grid.png", bbox_inches='tight')


def generate_report(years, obszary, sectors):
    sectors_names = ["rolnictwo", "gornictwo", "przetworstwo", "zaopatrywanie", "budownictwo", "transport"]
    obszary_names = ["bars", "heatmap", "districtmap"]
    year_from = years[0].get()
    year_to = years[1].get()
    if year_from > year_to:
        return
    size = int(year_to) - int(year_from)
    for i in range(0, len(obszary)):
        if obszary[i].get() == 1:
            print(i)
            if obszary_names[i] == "heatmap":
                if size > 0:
                    generate_grid(year_from, year_to, "heatmap_", 4)
            if obszary_names[i] == "districtmap":
                if size > 0:
                    generate_grid(year_from, year_to, "odszkodowania_", 3)
                    generate_grid(year_from, year_to, "odszkodowania_kwota_", 3)
            if obszary_names[i] == "bars":
                if size > 0:
                    for j in range(0, len(sectors)):
                        if sectors[j].get() == 1:
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Age", "Hard")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Age", "Deaths")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Age", "Total")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Months", "Hard")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Months", "Deaths")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Months", "Total")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Practice", "Hard")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Practice", "Deaths")
                            generate_grid_bar(year_from, year_to, sectors_names[j], "Practice", "Total")
    Generate_Pdf.generate(year_from, year_to, obszary, sectors)


def create_gui():
    root = tk.Tk()
    w = 640
    h = 350
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.title("Generator raportow dotyczacych wypadkow podczas pracy")
    #lata
    frame = tk.Frame()
    tk.Label(frame, text="Lata:").pack(side=tk.TOP)
    tk.Label(frame, text="Od:").pack(side=tk.LEFT, padx=5)
    yearFromVar = tk.StringVar()
    yearToVar = tk.StringVar()
    yearFrom = ttk.Combobox(frame, state='readonly', textvariable=yearFromVar, values=("2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"))
    yearFrom.set("2009")
    yearFrom.pack(side=tk.LEFT)
    tk.Label(frame, text="Do:").pack(side=tk.LEFT, padx=5)
    yearTo = ttk.Combobox(frame, state='readonly', textvariable=yearToVar, values=("2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"))
    yearTo.set("2016")
    yearTo.pack(side=tk.LEFT)
    frame.pack(pady=10)
    #obszary
    frameObszary = tk.Frame()
    tk.Label(frameObszary, text="Obszary:").pack()
    bar_plots = tk.IntVar()
    heat_map = tk.IntVar()
    district_map = tk.IntVar()
    tk.Checkbutton(frameObszary, text="Wykresy slupkowe liczby wypadkow", variable=bar_plots).pack()
    tk.Checkbutton(frameObszary, text="Mapa cieplna umiejscowienia urazu", variable=heat_map).pack()
    tk.Checkbutton(frameObszary, text="Porownanie wojewodztw ze wzgledu na liczbe odszkodowan", variable=district_map).pack()
    frameObszary.pack(pady=10)
    #sektory
    frameSektory = tk.Frame()
    rolnictwo = tk.IntVar()
    gornictwo = tk.IntVar()
    przetworstwo = tk.IntVar()
    zaopatrzenie = tk.IntVar()
    budownictwo = tk.IntVar()
    transport = tk.IntVar()
    tk.Label(frameSektory, text="Sektory gospodarcze:").grid(row=0, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Rolnictwo", variable=rolnictwo).grid(row=1, column=0, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Gornictwo", variable=gornictwo).grid(row=1, column=1, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Przetworstwo przemyslowe", variable=przetworstwo).grid(row=2, column=0, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Zaopatrywanie w energie elektryczna, gaz, wode", variable=zaopatrzenie).grid(row=2, column=1, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Budownictwo", variable=budownictwo).grid(row=3, column=0, stick=tk.W)
    tk.Checkbutton(frameSektory, text="Transport", variable=transport).grid(row=3, column=1, stick=tk.W)
    frameSektory.pack(pady=10)
    years = [yearFromVar, yearToVar]
    obszary = [heat_map, district_map, bar_plots]
    sectors = [rolnictwo, gornictwo, przetworstwo, zaopatrzenie, budownictwo, transport]
    tk.Button(root, text="Wygeneruj raport", command=lambda: generate_report(years, obszary, sectors)).pack(pady=10)
    root.mainloop()

create_gui()
