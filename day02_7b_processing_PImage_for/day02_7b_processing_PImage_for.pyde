#day02_7b_processing_PImage_for
img=None #沒有東西
def setup():
    global img 
    size(500,100)
    img=loadImage("cat.png")
    
def draw():
    for i in range(5):
        image (img,i*100,0,100,100)
