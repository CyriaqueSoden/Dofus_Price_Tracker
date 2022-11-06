import time
from PIL import Image
from screeninfo import get_monitors
import csv
import pyautogui
import pipreqs
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


time.sleep(5)
im = pyautogui.screenshot(region=(500, 500, 10, 10))
im2 = pyautogui.screenshot(region=(600, 600, 10, 10))

if im == im2:
    print("okkk")
