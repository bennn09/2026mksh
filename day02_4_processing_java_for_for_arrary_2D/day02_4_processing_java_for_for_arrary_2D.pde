//day02_4_processing_java_for_for_arrary_2D
PImage img;
int [][]a={
  {1,1,1,1,1},
  {1,1,1,1,1},
  {1,1,1,1,1} };
void mousePressed(){
  int i=mouseY/100,j=mouseX/100;
  if (mouseButton==LEFT)a[i][j]=0;//左鍵消失
  else a[i][j]=1;//右鍵恢復貓咪
}
void setup(){
  size(500,300);//寬度,長度
  img=loadImage("cat.png");
}
void draw(){
  background(255);
  for(int i=0;i<3;i++){//左手i 對應y
    for(int j=0;j<5;j++){//右手j 對應x
      if (a[i][j]==1) image(img,j*100,i*100,100,100);
    }
  }
}
