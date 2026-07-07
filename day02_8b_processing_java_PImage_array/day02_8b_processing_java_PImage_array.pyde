#day02_8b_processing_java_PImage_array
#把day02_5_processing_java__for_for_arrary_2D_mousePressed_cat_cat2放到AI翻譯
img = None
img2 = None

# 3×5 陣列
a = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

def setup():
    global img, img2
    size(500, 300)
    img = loadImage("cat.png")
    img2 = loadImage("cat2.png")

def draw():
    background(255)

    for i in range(3):
        for j in range(5):
            if a[i][j] == 1:
                image(img, j * 100, i * 100, 100, 100)
            elif a[i][j] == 2:
                image(img2, j * 100, i * 100, 100, 100)

def mousePressed():
    i = mouseY // 100
    j = mouseX // 100

    if 0 <= i < 3 and 0 <= j < 5:
        a[i][j] = (a[i][j] + 1) % 3
