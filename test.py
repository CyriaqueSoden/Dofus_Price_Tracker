import re
import time
from PIL import Image
from screeninfo import get_monitors
import csv
import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


analyse = pytesseract.image_to_string(
    r'C:\Users\maste\Pictures\bot\scsc100.Png').replace(" ", "")

test = re.sub(r"\D", "", "sdkjh987978asd098as0980a98sd")
print(test)
