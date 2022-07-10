import sys
from img2pdf import convert_from_path as path
import os

filepath = sys.argv[0]
if os.path.isdir(filepath):
    with open("output.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(path.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(path.convert(filepath))
else:
    print("please input image or image directory")

