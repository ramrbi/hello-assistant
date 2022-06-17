import qrcode

r=input("paste your link here:")
img= qrcode.make(
    r
)
img.save("qrcode.png")
img.show()