import turtle as t
def AF(size,n):
    if n == 0:
        t.fd(size)
    else:
        for i in [0,90,-90,-90,90]:
            t.lt(i)
            AF(size/3,n-1)
AF(200,2)
