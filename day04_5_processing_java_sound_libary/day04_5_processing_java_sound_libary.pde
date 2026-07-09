//day04_5_processing_java_sound_libary
import processing.sound.*;//使用Sound外掛

void setup(){//設定函式
  size(400,400);//視窗大小
  //將檔案拉進程式裡
  SoundFile music=new SoundFile(this,"music.mp3"); 
  music.play();//播放
}

void draw(){
     background(213,216,242);
}
