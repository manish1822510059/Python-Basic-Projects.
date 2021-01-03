import pyqrcode

data = "Name:- Manish kumar \n Email:-imanish1998@gamil.com"
img = pyqrcode.create(data)
img.png('detail.png',scale=10)