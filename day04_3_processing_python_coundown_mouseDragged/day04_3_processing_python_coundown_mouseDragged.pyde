#day04_3_processing_python_coundown_mouseDragged
#修改自 day04_2_processing_python_coundown_start_
#希望mouse左鍵dragged拖曳 改時間
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
    
def mouseDragged ():#mouse往上、往下滑
    global t#會修改t的值
    t-=(mouseY-pmouseY)#向量的差
    t=max(0,min(59,t))#限制在0-59之間
