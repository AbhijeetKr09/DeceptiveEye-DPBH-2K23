# extract text from image 
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Load the image
filename = '<image name>.png'
img = np.array(Image.open(filename))

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)