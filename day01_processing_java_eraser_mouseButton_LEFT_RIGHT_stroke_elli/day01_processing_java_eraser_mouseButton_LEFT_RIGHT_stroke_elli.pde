//day01_processing_java_eraser_mouseButton_LEFT_RIGHT_stroke_ellips
//有橡皮擦的版本
void setup(){//設定的函式
  size(500,500);//視窗
 background(255);//白色背景
}
void draw(){//畫圖的函式
  //如果mouse按下去
  if(mousePressed && mouseButton==LEFT){//mouse左鍵按下去
    stroke(225,0,0);//紅色的線
    line(mouseX,mouseY,pmouseX,pmouseY);
    //畫線 從mouse座標 到pmouse座標
 }
 if(mousePressed && mouseButton==RIGHT){//mouse右鍵按下去
  noStroke();//不要畫線
  ellipse(mouseX,mouseY,20,20);//畫20x20的圓,蓋掉畫錯的線
  }
}
