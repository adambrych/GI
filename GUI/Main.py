import tkinter as tk
from tkinter import ttk

def generate_report(years, obszary, sectors):
    print(sectors[0].get())

root = tk.Tk()

w = 640
h = 480
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
tk.Checkbutton(frameObszary, text="Porownanie wojewodztw ze wzgledu na liczbe wypadkow", variable=district_map).pack()
frameObszary.pack(pady=10)
#sektory
frameSektory = tk.Frame()
rolnictwo = tk.IntVar()
gornictwo = tk.IntVar()
przetworstwo = tk.IntVar()
zaopatrzenie = tk.IntVar()
budownictwo = tk.IntVar()
handel = tk.IntVar()
transport = tk.IntVar()
gastronomia = tk.IntVar()
informacja = tk.IntVar()
finanse = tk.IntVar()
nieruchomosci = tk.IntVar()
nauka = tk.IntVar()
administracja = tk.IntVar()
edukacja = tk.IntVar()
zdrowie = tk.IntVar()
tk.Label(frameSektory, text="Sektory gospodarcze:").grid(row=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Rolnictwo", variable=rolnictwo).grid(row=1, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Gornictwo", variable=gornictwo).grid(row=1, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Przetworstwo przemyslowe", variable=przetworstwo).grid(row=2, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Zaopatrywanie w energie elektryczna, gaz, wode", variable=zaopatrzenie).grid(row=2, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Budownictwo", variable=budownictwo).grid(row=3, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Handel", variable=handel).grid(row=3, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Transport", variable=transport).grid(row=4, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Gastronomia", variable=gastronomia).grid(row=4, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Informacja i komunikacja", variable=informacja).grid(row=5, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Dzialanosc finansowa", variable=finanse).grid(row=5, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Rynek nieruchomosci", variable=nieruchomosci).grid(row=6, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Dzialanosc naukowa i techniczna", variable=nauka).grid(row=6, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Administracja", variable=administracja).grid(row=7, column=0, stick=tk.W)
tk.Checkbutton(frameSektory, text="Edukacja", variable=edukacja).grid(row=7, column=1, stick=tk.W)
tk.Checkbutton(frameSektory, text="Opieka zdrowotna", variable=zdrowie).grid(row=8, column=0, stick=tk.W)
frameSektory.pack(pady=10)
years = [yearFromVar, yearToVar]
obszary = [bar_plots, heat_map, district_map]
sectors = [rolnictwo, gornictwo, przetworstwo, zaopatrzenie, budownictwo, handel, transport, gastronomia, informacja, finanse, nieruchomosci, nauka,
           administracja, edukacja, zdrowie]
button = tk.Button(root, text="Wygeneruj raport", command=lambda: generate_report(years, obszary, sectors)).pack(pady=10)
root.mainloop()

