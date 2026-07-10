#day05_4_processing_python_cos_sin_pikmin
#修改自day05_3_processing_python_cos_sin_pikmin
#加上殘影
def setup():
    size(400,300)#400x300的一半為(200,150)

def draw():
    background(54,39,155)
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/10+1)
        #rect(200+100*cos(a)-25,150+80*sin(a)-25,50,50) #手動移25
        rectMode(CENTER)#改為直接對齊「正中心」
    for r in range(-3,1): #殘影
        fill(255,255/(-r+1))
        rect(200+100*cos(a+r*0.1),150+80*sin(a+r*0.1),50,50)    
