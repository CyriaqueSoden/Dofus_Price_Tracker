from PIL import Image
from screeninfo import get_monitors
import csv
import pyautogui
import pipreqs
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


pathImg = r'C:\Users\maste\Pictures\bot\screen00.png'

analyse = pytesseract.image_to_string(
    Image.open(pathImg)).replace(" ", "")


print(analyse)
