#day03_6_processing__python_countdown
#修改自day03_5_processing__python_countdown
#有時會變負數、太快開始、不能暫停
#(1)用max()找最大值max(負數,0)
#(2)鬧鐘要以「修改」用mouseDgrassed來滑動
#(3)要以暫停
target=0#目標時間
target0=0#現在設定、要倒數的秒數
def mouseDragged():
    global target0
    target=mouseY-pmouseY
    target0-=min(59,target0) #不能超過59
    target0-=max(0,target0) #不能小於0
    
def setup (): #設定函式 
    global target #要可以修改外面target的變數
    size(500,200)
    m=minute() #分鐘(現在的時間)
    s=second() #秒數(現在的時間)
    target=(mm+5)*60+ss #我們的target目標時間
    
def draw():
    background(0)#背景色
    textSize(150) #字大小
    #text("00:00",80,150)#測式大小、位置用的
    remain=max(0,target-minute()*60-second(),0)#剩下的秒數
    mm=remain//60 #分鐘
    ss=remain%60  #秒數
    text(nf(mm,2)+":"+nf(ss,2),80,150)#接成數字
