//day02_1_processing_java_PImage_loadImage_image
size(600,300);//視窗大小
PImage img;//宣告圖片的變數
img=loadImage("penghu.png");//讀入圖片
image(img,0,0,600,300);//畫出圖片,在(0,0) 大小600x300
