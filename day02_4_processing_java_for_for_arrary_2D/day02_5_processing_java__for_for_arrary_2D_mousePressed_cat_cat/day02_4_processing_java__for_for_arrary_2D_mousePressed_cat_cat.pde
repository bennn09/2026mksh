//day02_5_processing_java__for_for_arrary_2D_mousePressed_cat_cat2
PImage img,img2;
int [][]a={//陣列的宣告
  {1,1,1,1,1},
  {1,1,1,1,1},
  {1,1,1,1,1} };
void mousePressed(){
  int i=mouseY/100,j=mouseX/100;
  a[i][j]=(a[i][j]+1)%3;
  //取餘數,1 2 3 變為0 1 2 0 1 2...
}
void setup(){
  size(500,300);//寬度,長度
  img=loadImage("cat.png");
  img2=loadImage("cat2.png");
}
void draw(){
  background(255);
  for(int i=0;i<3;i++){//左手i 對應y
    for(int j=0;j<5;j++){//右手j 對應x
      if (a[i][j]==1) image(img,j*100,i*100,100,100);
      if (a[i][j]==2) image(img2,j*100,i*100,100,100);
    }
  }
}
