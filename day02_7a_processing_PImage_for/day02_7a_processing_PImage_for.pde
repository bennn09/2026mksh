//day02_7a_processing_PImage_for
PImage img;
void setup(){
  size(500,100);
  img=loadImage("cat.png");
}
void draw(){
  for(int i=0;i<5;i++){
    image(img,i*100,0,100,100);
  }
}
  
