from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cwd = os.getcwd()
dir_path = os.path.join(cwd, "Modification")
img_folder_path = os.path.join(dir_path, "images")

for file in os.listdir(img_folder_path):
    print(f"Processing {file}...")
    img_path = os.path.join(img_folder_path, file)

    img = Image.open(img_path)

    text = pytesseract.image_to_string(img)

    print(f"Text extracted from {file}:\n{text}\n")
