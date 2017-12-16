import Readers.SVG_Body_Reader as SVG_Body_Reader


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
    SVG_Body_Reader.set_color(body_parts, "chest", rgb(0.9))
    SVG_Body_Reader.save_svg(doc)

generate_heatmap()

