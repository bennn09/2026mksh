#day05_6_processing_python_firework_arrow
#修改自day05_5_processing_python_firework_cos_sin
def setup():
    size(500,500)#中心為(250,250)

def draw():
    background(0)
    stroke(255,255,0)#線條為黃色
    for i in range(40):
        R=20+mouseX#花火的爆炸半徑，是20+mouseX
        a=(PI*2/40)*i#圓/7*i會有不同的角度
        #line(250,250,250+R*cos(a),250+R*sin(a))
        #黑色的線，從中心(250,250)往半徑的大圓發射出去
        line(250+(R-20)*cos(a),250+(R-20)*sin(a),250+R*cos(a),250+R*sin(a))
        #黃色的線,從（R-20）距離,射到R距離（往外）
