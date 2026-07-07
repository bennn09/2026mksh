//day02_2_processsing_java_void_draw_image
PImage img;
void setup(){//設定函式
  size(500,300);
  img=loadImage("cat.jpg");//要拉入cat.png進來
}
void draw(){
  background(225);//白色背景
  image(img, mouseX,mouseY,100,100);//秀圖片,放在mouse座標
}
