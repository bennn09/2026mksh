#day05_5_processing_python_firework_cos_sin
#花火節煙火,先畫出「往外射出20條線」
def setup():
    size(500,500)#中心為(250,250)

def draw():
    background(255,255,242)
    for i in range(20):
        R=20+mouseX#花火的爆炸半徑，是20+mouseX
        a=(PI*2/20)*i#圓/7*i會有不同的角度
        line(250,250,250+R*cos(a),250+R*sin(a))
        #黑色的線，從中心(250,250)往半徑的大圓發射出去
