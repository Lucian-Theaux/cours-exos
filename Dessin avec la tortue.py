from turtle import *
setup(640, 480)
speed(200)

def carre(n):
    """
    La fonction carre() crée un carré de côté 'n'
    n -> Taille du côté
    """
    for i in range(4):
        fd(n)
        lt(90)

def suite_carre(n, nb):
    """
    La fonction suite_carre() crée une suite de 'nb' carré avec une taille 'n' de côté
    n -> Taille des côtés des carrés
    nb -> Nombre de carrés 
    """
    for i in range(nb):
        carre(n)
        fd(n)

def suite_carre2(n, nb):
    """
    La fonction suite_carre2() crée une suite de 'nb' carré avec une taille 'n' de côté avec un écart de: n + 0.2*n
    n -> Taille des côtés des carrés
    nb -> Nombre de carrés 
    """
    for i in range(nb):
        carre(n)
        fd(n)
        up()
        fd(n + 0.2*n)
        down()

def carre_in_carre(n):
    """
    Crée un grand carré avec 4 petits carrés de 'n' taille
    n -> Taille des côtés des petits carrés
    """
    for i in range(4):
        suite_carre(n,2)
        lt(90)
# carre_in_carre(50)

def croise(n, ecart):
    """
    La fonction croise() crée une figure avec 4 carrés aux extrémités d'un seul grand carré.
    n -> Taille des petits carré
    nb -> Ecart séparant les petits carrés formant le grand carré.
    """
    for i in range(4):
        fd(n)
        lt(90)
        fd(ecart)
        lt(90)
        fd(n)
        lt(90)
# croise(10, 40)

def escalier(n, nb):
    """
    La fonction escalier() crée un esalier de 'nb' marche de taill 'n'
    n -> Taille des escaliers
    nb -> Nombre d'escaliers
    """
    # bgcolor('cyan')
    # color("white")
    # fillcolor()
    # begin_fill()
    # up()
    # goto(-300,  200)
    # write("Stairs to Paradise", font=("Helvatica", 16))
    # goto(-320, -240)
    # down()
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
    # end_fill()

# escalier(50, 50)

# def avancer():
#     fd(10)
# def droite():
#     rt(90)
# def gauche():
#     lt(90)
# def derriere():
#     rt(180)
#     fd(10)

# onkey(avancer, "Up")
# onkey(droite, "Right")
# onkey(gauche, "Left")
# onkey(derriere, "Down")
# listen()

## Ex 7
def rosace(nb_cotes, logueur, nb_poly):
    for i in range(nb_poly):
        for j in range(nb_cotes):
            fd(logueur)
            lt(360/nb_cotes)
        rt(360/nb_poly)
# rosace(6,100,6)
# rosace(6,100,24)
# rosace(4,100,12)

## Ex 8
def rosace2(nb_cotes, logueur, nb_poly):
    for i in range(nb_poly):
        for j in range(nb_cotes):
            fd(logueur)
            lt(360/nb_cotes)
        fd(logueur)
        rt(360/nb_poly)
# rosace2(4,50,6)
# rosace2(5,50,6)
# rosace2(6,50,6)

# ____________________________________________________________________________________________________________
## Ex 9
def carres_imbriques(n):
    longueur = 10
    for i in range(n):
        carre(longueur)
        longueur += 10
# carres_imbriques(10)
# ____________________________________________________________________________________________________________
## Ex 10
def carres_imbriques2(n):
    longueur = 10
    for i in range(n):
        carre(longueur)
        longueur *= 2
# carres_imbriques2(5)

def carres_imbriques3(n):
    longueur = 10
    for i in range(n):
        carre_in_carre(longueur)
        longueur *= 2
# carres_imbriques3(5)
# ____________________________________________________________________________________________________________
## Ex 11
def spirale(n):
    longueur = 2
    for i in range(n):
        fd(longueur)
        lt(90)
        longueur += 2
# spirale(1000)
# ____________________________________________________________________________________________________________
## Ex 12
def polygone(n, nb):
    for i in range(nb):
        fd(n)
        lt(360/nb)
    
def suite(n, nb):
    for i in range(3,3+nb):
        polygone(n, i)


def suite2(n, nb):
    for i in range(3,3+nb):
        polygone(n, i)
        fd(n)
        up()
        fd(n)
        down()
# suite(20, 10)

def suite3(n, nb):
    for i in range(3,3+nb):
        polygone(n, i)
        fd(n)
        rt(360/nb)

def suite4(nb):
    longueur = 5
    for i in range(nb):
        polygone(longueur, 4)
        fd(longueur)
        rt(360/6)
        longueur += longueur*(20/100)


suite4(15)

mainloop()
