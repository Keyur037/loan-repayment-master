import sys
import img2pdf
import os

filepath = r'C:\Users\DELL\.jenkins\workspac\loan-repayment-master\Convert_a_image_to_pdf'

if os.path.isdir(filepath):
    with open('output.pdf', "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"):
        with open('output.pdf', "wb") as f:
            f.write(img2pdf.convert(filepath))
else:
    print("please input correct image or correct image directory")

