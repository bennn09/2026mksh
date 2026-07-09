#day04_5_processing_python_sound_libary_bad
#Help-Examples
add_libary("sound")
music=None
def setup():
    globalmusic
    size (400,400)
    music=SoundFile(this,"music.mp3") #這行失敗了
    #music.play()
    
def draw():
    background(213,216,242)
#程式沒有錯，是相容性問題
    
