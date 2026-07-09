#day04_2_processing_python_coundown_start
#希望可以右鍵會開始跟暫停
def setup():
    size(400,400)
start=False#沒有開始  
t=10  
def draw():
    global t
    background(0)
    textSize(300)
    textAlign(CENTER,CENTER)
    text(t,200,200)
    if start and frameCount%60==0 and t>0:t-=1

def mousePressed ():
    global start
    if mouseButton==RIGHT:start=not start
    
