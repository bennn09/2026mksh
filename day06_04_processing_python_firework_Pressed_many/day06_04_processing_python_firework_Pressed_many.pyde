#day06_04_processing_python_firework_Pressed_many
#修改自day06_03_processing_python_firework_gravity_20
#想要做出互動的花火,且mouse可點很多次
def setup():
    size(500,500)

x,y=[],[]#一開始的座標
vx,vy=[],[]#一開始沒有速度
gx,gy=0,0.0098#加速度
N=0#現在有幾個火花?

def draw():
    background(0)
    fill(252,87,236)
    ellipse(mouseX,mouseY,10,10)
    for i in range(N):
        ellipse(x[i],y[i],10,10)
        x[i]+=vx[i]
        y[i]+=vy[i]
        vx[i]+=gx
        vy[i]+=gy
            
def mousePressed(): #mouse按下去,要射出火花
    global x,y,vx,vy,N #要修改外面的變數
    x+=[mouseX]*20
    y+=[mouseY]*20
    vx+=[2*cos(PI*2/20*i)for i in range(20)]
    vy+=[2*sin(PI*2/20*i)for i in range(20)]
    N+=20
    
    
