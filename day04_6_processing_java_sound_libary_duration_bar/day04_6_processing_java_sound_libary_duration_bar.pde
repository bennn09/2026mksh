//day04_6_processing_java_sound_libary_duration_bar
import processing.sound.*;//使用Sound外掛
float T;
void setup(){//設定函式
  size(400,50);//視窗大小
  //將檔案拉進程式裡
  SoundFile music=new SoundFile(this,"music.mp3"); 
  music.play();//播放
  T=music.duration();
}

void draw(){
     background(213,216,242);
     fill(244,247,202);
     rect(0,0,400*(frameCount/60.0)/T,50);
}
