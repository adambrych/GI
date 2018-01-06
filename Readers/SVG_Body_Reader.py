import xml.dom.minidom as dom
import Config
import time


def timestamp():
    return str(int(round(time.time() * 1000)))


def read_svg():
    doc = dom.parse(Config.IMG_PATH + "\\human_body.svg")
    paths = doc.getElementsByTagName("path")
    body_parts = dict()
    body_parts["head"] = []
    body_parts["neck"] = []
    body_parts["arms"] = []
    body_parts["legs"] = []
    body_parts["chest"] = []
    for element in paths:
        id = element.getAttribute("id")
        if id == "head":
            body_parts["head"].append(element)
        elif id == "neck":
            body_parts["neck"].append(element)
        elif id.find("arm") != -1:
            body_parts["arms"].append(element)
        elif id.find("Leg") != -1:
            body_parts["legs"].append(element)
        elif id.find("chest") != -1:
            body_parts["chest"].append(element)
    return doc, body_parts


def set_color(body_parts, part, color):
    element_array = body_parts[part]
    for element in element_array:
        style_string = element.getAttribute("style")
        style_string = style_string[12:]
        element.setAttribute("style", "fill:" + color + style_string)


def save_svg(doc):
    filename = "injury_heat_map_"+timestamp()+".svg"
    with open(Config.IMG_PATH + "\\" + filename, "w") as svg_file:
        doc.writexml(svg_file)
    return filename





