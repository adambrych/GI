
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.platypus import Image

heat = "Img/heatmap_2014.png"
age = "Plots/Age/Group/Liczba_wypadków_ze_względu_na_Wiek_w_sektorze_Rolnictwo,_leśnictwo,_łowiectwo_i_rybactwo_(A).png"
months = "Plots/Months/Group/Liczba_wypadków_ze_względu_na_Miesiąc_w_sektorze_Rolnictwo,_leśnictwo,_łowiectwo_i_rybactwo_(A).png"
practice = "Plots/Practice/Group/Liczba_wypadków_ze_względu_na_Staż_Pracy_w_sektorze_Rolnictwo,_leśnictwo,_łowiectwo_i_rybactwo_(A).png"

heat_img = utils.ImageReader(heat)
age_img = utils.ImageReader(age)
months_img = utils.ImageReader(months)
practice_img = utils.ImageReader(practice)
#img = utils.ImageReader(path)
#iw, ih = img.getSize()


canvas = canvas.Canvas("report.pdf", pagesize=letter)

canvas.setFont("Helvetica", 30)
canvas.drawString(140,750,'Raport z wypadków w pracy')
iw, ih = heat_img.getSize()
canvas.drawImage(heat_img, 20, 450, iw/2, ih/2)
canvas.setFont("Helvetica", 12)
canvas.drawString(20,420,'Mapa cieplna ciala')
iw, ih = age_img.getSize()
canvas.drawImage(age_img, 20, 70, iw/1.5, ih/1.5)
canvas.showPage()
iw, ih = months_img.getSize()
canvas.drawImage(months_img, 20, 450, iw/1.5, ih/1.5)
iw, ih = practice_img.getSize()
canvas.drawImage(practice_img, 20, 70, iw/1.5, ih/1.5)
canvas.save()