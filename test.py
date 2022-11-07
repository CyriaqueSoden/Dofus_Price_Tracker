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

print(analyse)

re.sub("[^0-9]", "", "aeeaz999,")
