# 新的密码方式
import turtle as t
import time
# 算法
def gap():
    t.pu()
    t.fd(2)
def sl(G):
    if G == 1 :
        gap()
        t.pd()
        t.fd(40)
        t.rt(90)
        gap()
    else :
        gap()
        t.pu()
        t.fd(40)
        t.rt(90)
        gap()
def sn(date):
    sl(1) if date in [2,3,4,5,6,8,9] else sl(2)
    sl(1) if date in [0,1,3,4,5,6,7,8,9] else sl(2)
    sl(1) if date in [0,2,3,5,6,8] else sl(2)
    sl(1) if date in [0,2,6,8] else sl(2)
    t.lt(90)
    sl(1) if date in [0,4,5,6,8,9] else sl(2)
    sl(1) if date in [0,2,3,5,6,7,8,9] else sl(2)
    sl(1) if date in [0,1,2,3,4,7,8,9] else sl(2)
    t.lt(180)
    t.pu()
    t.fd(20)
# 画笔设置
t.speed(10)
t.pensize(5)
t.pencolor("red")
# 时间获取
t.setup(1000,800,-500,0)
for i in time.strftime('%Y%m%d',time.gmtime()):
    sn(eval(i))
