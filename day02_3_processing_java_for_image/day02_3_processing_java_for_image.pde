//day02_3_processing_java_for_image
//練習for迴圈
PImage img;
void setup(){
  size(500,300);//寬度,長度
  img=loadImage("cat.png");
}

void draw(){
  background(225);
  for(int i=0;i<3;i++){//左手i 對應y
    for(int j=0;j<5;j++){//右手j 對應x
      image(img,j*100,i*100,100,100);
    }
  }
}
