
import cv2
import webbrowser as w

def decoder() :
    choose=input("if u want to de decode type 'd' or if u want to scan and move to web type 's':")
    if"s" in choose:
      t=input("paste the file name here:")
      d= cv2.QRCodeDetector()
      retval,points,staraight_qrcode =d.detectAndDecode(cv2.imread(t))
      w.open("https://www."+retval)
    elif "d" in choose:

        t=input("paste the file name here:")
        d= cv2.QRCodeDetector()
        retval,points,staraight_qrcode =d.detectAndDecode(cv2.imread(t))
        print(retval)


decoder()

