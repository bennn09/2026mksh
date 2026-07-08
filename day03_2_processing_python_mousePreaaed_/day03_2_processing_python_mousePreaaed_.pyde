#day03_2_processing_python_mousePreaaed_
#修改自day03_1_processing_python_textSize_text
a=[99,88,77,66,55]

def mousePressed():#mouse按下去,對應
    i=mouseX//100#i跟mouse換算關係
    if mouseButton==LEFT:a[mouseX//100]+=1#按左鍵a[i]加1
    else:a[mouseX//100]-=1 #按右鍵,a[i]減1
    
def setup (): #設定函式
    size (500,100)
def draw ():#畫圖的函式 
    for i in range(5):#迴圈跑五次
        fill(255,255,242)
        rect(i*100,0,100,100)#畫格子
    
        fill(255,0,0)#紅色的字
        textSize(80)
        text(a[i],i*100,80)#畫出a[i]
