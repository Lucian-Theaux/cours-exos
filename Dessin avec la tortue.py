from turtle import *
setup(640, 480)

def carre(n):
    for i in range(4):
        fd(n)
        lt(90)

def suite_carre(n, nb):
    for i in range(nb):
        carre(n)
        fd(n)

def suite_carre2(n, nb):
    for i in range(nb):
        carre(n)
        fd(n)
        up()
        fd(n + 0.2*n)
        down()

def carre_in_carre(n):
    for i in range(4):
        suite_carre(n,2)
        lt(90)

def croise(n, ecart):
    for i in range(4):
        fd(n)
        lt(90)
        fd(ecart)
        lt(90)
        fd(n)
        lt(90)

def escalier(n, nb):
    bgcolor('cyan')
    color("white")
    fillcolor()
    begin_fill()
    up()
    goto(-300,  200)
    write("Stairs to Paradise", font=("Helvatica", 16))
    goto(-320, -240)
    down()
    for i in range(nb):
        lt(90)
        fd(n)
        rt(90)
        fd(n)
    rt(90)
    for i in range(nb):
        fd(n)
    rt(90)
    for i in range(nb):
        fd(n)
    end_fill()

escalier(10, 80)
mainloop()
