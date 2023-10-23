from PIL import Image
import pytesseract
import numpy as np

def main():
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    filename = '7_hazi/street.jpg'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    #hibasan olvassa be a kepet

    incorrect_letters = []
    for c in text:
        if c not in "01":
            incorrect_letters.append(c)
    for c in incorrect_letters:
        text = text.replace(c,"0")
    x = text.split("\n")
    #ezzel megprobaltam kijavitani
    for i in range(len(x)):
        print(i)
        print(x[i])
        print(chr(int(x[i], 2)))
    

if __name__ == "__main__":
    main()