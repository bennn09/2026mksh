#day05_2_processing_python_cos_sin_dragon_ball_move
#想讓7顆龍珠「轉動」
def setup():
    size(400,400)

def draw ():#畫圖函式
    background(0) #背景 黑色
    for i in range(7):#七顆龍珠，跑七次迴圈
        #a=(PI*2/7)*i+mouseX/1000.0 #轉動,靠角度增加
        a=(PI*2/7)*i+radians(frameCount)/5 #轉動
        ellipse(200+150*cos(a),200+150*sin(a),80,80)
         
