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