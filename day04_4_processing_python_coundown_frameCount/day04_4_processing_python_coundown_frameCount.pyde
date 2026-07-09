#day04_4_processing_python_coundown_frameCount
#希望了解day04_3_的frameCount意思
def setup():
    size(400,400)
    frameRate(5)#等一下刪除
#如果想知道現在是第幾次執行void draw()要用t來數
t=1 #第一行，宣告t變數
def draw():
    global t#第2行，要認識外面的t
    background(0)
    textSize(100)
    textAlign(CENTER,CENTER)
    text(frameCount,200,100)#值會跟第4行的t一樣
    
    text(t,200,200)#第3行，試著畫出t的值
    t+=1#第4行，每次結束時t會「加一」
    
    text(frameCount//60,200,300)#每60次，//60變秒
    
