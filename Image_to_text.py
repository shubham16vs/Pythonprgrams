import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\TesseractOCR\\tesseract.exe'
img = Image.open("sample.jpg")
text = pytesseract.image_to_string(img)
print(text)