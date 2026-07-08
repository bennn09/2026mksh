#day03_5_processing__python_countdown
#修改自day03_4_processing__python_countdown
#倒數計時,先印時間
target=0
def setup (): #設定函式 
    global target #要可以修改外面target的變數
    size(500,200)
    mm=minute() #分鐘(現在的時間)
    ss=second() #秒數(現在的時間)
    target=(mm+5)*60+ss #我們的target目標時間
    
def draw():
    background(0)#背景色
    textSize(150) #字大小
    #text("00:00",80,150)#測式大小、位置用的
    remain=target-minute()*60-second()#剩下的秒數
    mm=remain//60 #分鐘
    ss=remain%60  #秒數
    text(nf(mm,2)+":"+nf(ss,2),80,150)#接成數字
