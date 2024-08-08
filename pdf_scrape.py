import fitz

with fitz.open("files/animalpdf/Bumblebee.pdf") as pdf:
    p1 = pdf[0].get_text()
    print(p1)