import pyqrcode


while True:
    text = input("enter a text or url to change to qrcode :\n")
    qr_code = pyqrcode.create(text)
    i =input("enter name for the ")
    qr_code.png(i +".png", 1 )
    stop_sestem = input("do you want to make anther qrcood[yas , no] :\n")
    if stop_sestem == "no":
        break






