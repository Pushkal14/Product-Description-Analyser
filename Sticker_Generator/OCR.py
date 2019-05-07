import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img_path = './Stickers_Generated_Liberation-Mono/1.png'
ocr_text = pytesseract.image_to_string(img_path)
ocr_text = list(ocr_text.split('\n'))
for _ in range(len(ocr_text)):
    try:
        ocr_text.remove('')
    except ValueError:
        break
length = len(ocr_text)
for i in range(length//2):
    print("%20s %20s" %(ocr_text[i], ocr_text[length//2+i]))
