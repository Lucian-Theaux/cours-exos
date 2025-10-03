# Droit et propriété de Lucian Théaux 1°2 (lol)

from turtle import *
from nsi_ui import *
speed(0)

def polygone(n, nb):
    """
    Fonction suplémentaire pour les fonctions suivante, crée un polygine de 'n' longueur et 'nb' côtés
    """
    for i in range(nb):
        fd(n)
        lt(360/nb)

def creer_polygone():
    """
    Fonction sans paramètre que l'on va associer au bouton
    """
    polygone(get_int(tirette_taille),get_int(tirette_cote))

def effacer():
    """
    Effacer le canva
    """
    clearscreen()
    showturtle()

def avancer():
    """
    Avance de 10 sur turtle
    """
    setheading(90)
    fd(10)
def droite():
    """
    Tourne à droite et avance 10 sur turtle
    """
    setheading(0)
    fd(10)
def gauche():
    """
    Tourne à gauche et avance 10 sur turtle
    """
    setheading(180)
    fd(10)
def arriere():
    """
    Va en arrière de 10
    """
    setheading(270)
    fd(10)

button("Polygone", creer_polygone)
button("Effacer", effacer)

tirette_taille = slider("Taille", 10, 100)
tirette_cote = slider("Côté", 3, 100)

onkey(avancer, 'z')
onkey(gauche, 'q')
onkey(droite, 'd')
onkey(arriere, 's')
listen()

mainloop()