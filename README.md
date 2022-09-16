1. Textinput.txt file contains the article.

2. lines.py import the article and broke the articles into lines

3. main.py take the lines , font and generate image with Pillow package




pip install pytesseract Pillow

import os
import pytesseract
from PIL import Image

path='.'
text=""
f = open("/content/output.txt", "w")
f.write(text)
f.close()
for r, d, f in os.walk(path):
    f.sort()
    for file in f:
        print(file+"\n")
        output=pytesseract.image_to_string(Image.open(file), lang='bangla_2_1')#Bengali+Arabic
        output+="\n"
        print(output)
        f = open("/content/output.txt", "a")
        f.write(output)
        f.close()
