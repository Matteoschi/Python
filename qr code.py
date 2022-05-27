import time
import qrcode
from pyzbar.pyzbar import decode
import cv2
todo = input("premere C per fare un qr premere S per scanzionare un qr ")
if todo == ("C"):
    codice = input("inserire cosa scrivere nel qr code ")
    img=qrcode.make(codice)
    img.save('qr code.png')
    img
if todo == ("S"):
    a = input("scrivere nome img es qrcode.png ")
    img = cv2.imread(a)
    code = decode(img)
    for barcode in decode(img):
        print(barcode.data)
        text = barcode.data.decode('utf-8')
        print(text)
time.sleep(50)


