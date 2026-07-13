#day06_05_processing_python_firework_mousePressed_fill_r_g_b
#修改自 day06_04_processing_python_firework_Pressed_many
#花火想做成不同顏色
def setup():
    size(900,900)

x,y=[],[]#一開始的座標
vx,vy=[],[]#一開始沒有速度
gx,gy=0,0.0098#加速度
N=0#現在有幾個火花?
r,g,b=[],[],[]#每個火花的顏色

def draw():
    background(0)
    fill(252,87,236)
    ellipse(mouseX,mouseY,10,10)
    for i in range(N):
        fill(r[i],g[i],b[i])
        ellipse(x[i],y[i],10,10)
        x[i]+=vx[i]
        y[i]+=vy[i]
        vx[i]+=gx
        vy[i]+=gy

def mousePressed(): #mouse按下去,要射出火花
    global r,g,b,x,y,vx,vy,N,r,g,b #要修改外面的變數
    x+=[mouseX]*20
    y+=[mouseY]*20
    vx+=[2*cos(PI*2/20*i)for i in range(20)]
    vy+=[2*sin(PI*2/20*i)for i in range(20)]
    r+=[random(255)]*20
    g+=[random(255)]*20
    b+=[random(255)]*20
    N+=20
