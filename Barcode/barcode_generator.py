import barcode
from barcode.writer import ImageWriter


def barcode_svg():
    barcode1 = barcode.get('code128', 'shantanu199')
    barcode1.save('barcode1')


def barcode_image():
    barcode2 = barcode.get('code128', 'shantanu199', writer=ImageWriter())
    barcode2.save('barcode2')


# barcode_svg()
barcode_image()
