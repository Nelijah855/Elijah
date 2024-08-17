from PIL import Image


image=Image.open('icon.png')
def all():
    for i in range(512):
        for x in range(512):
            a=list(image.getpixel((i,x)))
            a[2]=203
            print(a)
            print(i,'.................................',x)

def data():
    dat=image.getdata()
    
    
data()
def show():
    
    image.show("pixelab")

show()
