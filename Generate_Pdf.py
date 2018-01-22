from reportlab.pdfgen import canvas as cnv
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
import os
import Config


def generate(year_from, year_to, obszary, sectors):
    canvas = cnv.Canvas("report.pdf", pagesize=letter)
    width, height = letter
    canvas.setFont("Helvetica", 20)
    canvas.drawString(190, 750, 'Raport z wypadków w pracy')

    #generate plots
    sectors_names = ["rolnictwo", "gornictwo", "przetworstwo", "zaopatrywanie", "budownictwo", "transport"]
    obszary_names = ["heatmap", "districtmap", "bars"]
    size = int(year_to) - int(year_from) + 1
    for i in range(0, len(obszary)):
        if obszary[i].get() == 1:
            if obszary_names[i] == "heatmap":
                canvas.setFont("Helvetica", 14)
                canvas.drawString(20, 710, 'Mapy cieplne umiejscowienia urazu:')
                page_width = 100
                page_height = 430
                for j in range(0, size):
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "heatmap_" + str(int(year_from)+j) + ".png")
                    iw, ih = img.getSize()
                    if j % 2 == 1 and page_width + iw/2 < width:
                        page_width += iw/2 + 20
                    elif page_width > 100:
                        page_width = 100
                        page_height -= ih/2 + 20
                    canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                    if page_height <= ih/2 and page_width > 100:
                        page_height = 750 - ih/2
                        page_width = 100
                        canvas.showPage()
                page_width = 20
                if size > 4:
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "heatmap_grid.png")
                    iw, ih = img.getSize()
                    if size > 4:
                        page_height = 750 - ih/2
                        if size % 4 != 0:
                            canvas.showPage()
                    canvas.drawImage(img, page_width, page_height, iw/2.2, ih/2, mask="auto")
                    canvas.showPage()
                else:
                    if size != 4:
                        canvas.showPage()
            elif obszary_names[i] == "districtmap":
                print('district')
                page_width = 20
                page_height = 550
                canvas.drawString(page_width, 750, 'Kartogramy liczby wyplaconych odszkodowan:')
                for j in range(0, size):
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "odszkodowania_" + str(int(year_from)+j) + ".png")
                    iw, ih = img.getSize()
                    if j % 2 == 1 and page_width + iw/2 < width:
                        page_width += iw/2 + 20
                    elif page_width > 20:
                        page_width = 20
                        page_height -= ih/2 + 20
                    canvas.drawImage(img, page_width, page_height, iw/2.3, ih/2, mask="auto")
                    if page_height <= ih/2 and page_width > 20:
                        page_height = 750 - ih/2
                        page_width = 20
                        canvas.showPage()
                page_width = 20
                if size > 6:
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "odszkodowania_grid.png")
                    iw, ih = img.getSize()
                    if size > 6:
                        page_height = 750 - ih/2
                        canvas.showPage()
                    canvas.drawImage(img, page_width, page_height, iw/2.2, ih/2, mask="auto")
                    canvas.showPage()
                else:
                    if size != 6:
                        canvas.showPage()
                print('bars')
                page_width = 20
                page_height = 550
                canvas.drawString(page_width, 750, 'Kartogramy kwoty wyplaconych odszkodowan:')
                for j in range(0, size):
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "odszkodowania_kwota_" + str(int(year_from)+j) + ".png")
                    iw, ih = img.getSize()
                    if j % 2 == 1 and page_width + iw/2 < width:
                        page_width += iw/2 + 20
                    elif page_width > 20:
                        page_width = 20
                        page_height -= ih/2 + 20
                    canvas.drawImage(img, page_width, page_height, iw/2.5, ih/2, mask="auto")
                    if page_height <= ih/2 and page_width > 20:
                        page_height = 750 - ih/2
                        page_width = 20
                        canvas.showPage()
                page_width = 20
                if size > 6:
                    img = utils.ImageReader(Config.IMG_PATH + "\\" + "odszkodowania_kwota_grid.png")
                    iw, ih = img.getSize()
                    if size > 6:
                        page_height = 750 - ih/2
                        canvas.showPage()
                    canvas.drawImage(img, page_width, page_height, iw/2.2, ih/2, mask="auto")
                    canvas.showPage()
                else:
                    if size != 6:
                        canvas.showPage()
            elif obszary_names[i] == "bars":
                page_height = 720
                page_width = 20
                canvas.drawString(page_width, 750, 'Wykresy slupkowe liczby wypadkow:')
                for j in range(0, len(sectors)):
                    if sectors[j].get() == 1:
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Age\\" + str(int(year_from)+k) + "\\Deaths\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Age\\" + str(int(year_from)+k) + "\\Hard\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Age\\" + str(int(year_from)+k) + "\\Total\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Months\\" + str(int(year_from)+k) + "\\Deaths\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Months\\" + str(int(year_from)+k) + "\\Hard\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Months\\" + str(int(year_from)+k) + "\\Total\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Practice\\" + str(int(year_from)+k) + "\\Deaths\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Practice\\" + str(int(year_from)+k) + "\\Hard\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        for k in range(0, size):
                            try:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Practice\\" + str(int(year_from)+k) + "\\Total\\" + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            except OSError:
                                print("Brak wykresu")
                        try:
                            for type in ["death_", "hard_", ""]:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Age\\Group\\"+type + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            for type in ["death_", "hard_", ""]:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Months\\Group\\"+type + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                            for type in ["death_", "hard_", ""]:
                                img = utils.ImageReader(Config.PLOTS_PATH + "\\Practice\\Group\\"+type + sectors_names[j] + ".png")
                                iw, ih = img.getSize()
                                page_height -= ih/2 + 20
                                canvas.drawImage(img, page_width, page_height, iw/2, ih/2, mask="auto")
                                if page_height <= ih/2:
                                    page_height = 730
                                    page_width = 20
                                    canvas.showPage()
                        except OSError:
                            print("Brak obrazka")



    canvas.save()
    os.startfile('report.pdf', 'open')
