import Readers.SVG_Body_Reader as SVG_Body_Reader
import Readers.Tabl15_Reader as InjuryReader
import cairosvg
import Config
import sys
from PIL import Image


def rgb(value):
    minimum = 0
    maximum = 1
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return '#%02x%02x%02x' % (r, g, b)


def generate_heatmap():
    doc, body_parts = SVG_Body_Reader.read_svg()
    injuries = InjuryReader.read_xlsx()
    body_parts_names = ["Glowa", "Tulow", "Grzbiet", "Rece", "Nogi", "Szyja"]
    for i in injuries:
        injury_count = injuries[i].iloc[0]
        sum = 0
        for j in body_parts_names:
            sum += injury_count[j]
        chest = (injury_count["Grzbiet"] + injury_count["Tulow"]) / sum
        head = injury_count["Glowa"] / sum
        arms = injury_count["Rece"] / sum
        legs = injury_count["Nogi"] / sum
        neck = injury_count["Szyja"] / sum
        SVG_Body_Reader.set_color(body_parts, "chest", rgb(chest))
        SVG_Body_Reader.set_color(body_parts, "head", rgb(head))
        SVG_Body_Reader.set_color(body_parts, "arms", rgb(arms))
        SVG_Body_Reader.set_color(body_parts, "legs", rgb(legs))
        SVG_Body_Reader.set_color(body_parts, "neck", rgb(neck))
        SVG_Body_Reader.save_svg(doc)
        cairosvg.svg2png(bytestring=doc.toxml(), write_to=Config.IMG_PATH + "/heatmap_temp_"+i+".png")
        scale_img = Image.open(Config.IMG_PATH + "\\heatmap_scale.png")
        heatmap_img = Image.open(Config.IMG_PATH + "\\heatmap_temp_"+i+".png")
        new_img = Image.new("RGBA", (340, 520))
        new_img.paste(heatmap_img, (0, 0))
        new_img.paste(scale_img, (250, 0))
        new_img.save(Config.IMG_PATH + "\\heatmap_"+i+".png")

generate_heatmap()

