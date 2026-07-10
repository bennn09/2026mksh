#day05_3_processing_python_cos_sin_pikmin
#抽獎勵(金色花苗)有轉動的動畫
def setup():
    size(400,300)#400x300的一半為(200,150)


def draw():
    background(54,39,155)
    noStroke()
    fill(255, 255, 255, 150) 
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/10+1)
        #rect(200+100*cos(a)-25,150+80*sin(a)-25,50,50) #手動移25
        rectMode(CENTER)#改為直接對齊「正中心」
        rect(200+100*cos(a),150+80*sin(a),50,50)
