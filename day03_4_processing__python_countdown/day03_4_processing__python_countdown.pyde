#day03_4_processing__python_countdown
#倒數計時,先印時間
def setup (): #設定函式
    size(500,200)
    
def draw():
    background(0)
    textSize(150) #字大小
    #text("00:00",80,150)#測式大小、位置用的
    mm=minute()#分鐘
    ss=second()#秒數
    text(nf(mm,2)+":"+nf(ss,2),80,150)#接成數字
