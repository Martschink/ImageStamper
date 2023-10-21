#! python3
C:\Users\treem\Documents\image_stamper.py
start notepad++ "C:\Users\treem\Documents\image_stamper.py"
from PIL import Image, ImageDraw
"C:\Users\treem\Dropbox\Mac Deford\CCDP_10-19-23\Photos-001\IMG_20231019_182702331 - Copy.jpg"


#img = Image.open('C:\\Users\\treem\\Dropbox\\Mac Deford\\CCDP_10-19-23\\Photos-001\\IMG_20231019_182702331 - Copy.jpg')
img2 = Image.open('C:\\Users\\treem\\Dropbox\\Mac Deford\\shared materials\\logo_white.png')
img2 = Image.open('C:\\Users\\treem\\Dropbox\\Mac Deford\\shared materials\\MCD23001_color small.png')

img.paste(img2, (img.width-(img2.width+60),img.height-(img2.height+60)))

In [49]: img.show()

img.paste(img2, (1000,400 ))

img.paste(img2, (img.width-(img2.width+20),img.height-img2.height+20))

MCD23001_color small.png

pic_files = os.listdir()
dirpath=os.getcwd()

for p in pic_files:
    img_path = dirpath+"\\"+p
    img = Image.open(img_path)
    img.paste(img2, (img.width-(img2.width+60),img.height-(img2.height+60)))
    print(p)
    img.save("stamped_"+p)
    
    https://www.dropbox.com/scl/fo/5ub6jdszgz9sfwlpa4m40/h?rlkey=68v39bqn7s1nv05u8hstp074w&dl=0