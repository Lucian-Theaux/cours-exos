from turtle import *

speed(100)
shape("turtle")
title("LA BEAUT2")
# Commande Carré de coté 'cote'
# cote = 100
#
# for i in range(4):
#     forward(cote)
#     right(90)
# print("Finit !")


## Commande Polygone de nombre de coté 'n' et de longueur 'cote' et d'angle 'angle'
# n = 50
# cote = 50
# angle = 360/n
# for i in range(n):
#     forward(cote)
#     right(angle)


# Focntion Polygone avec les paramètres 'n' et 'cote'

def polygone(n:int,cote:int):
    """ Tracer un polygone d'un nombre de côtés 'n' et de longueur 'cote' """

    angle = 360/n
    for i in range(n):
        if i == 1:
            down()
        else:
            up()
        forward(cote)
        right(angle)

def figure(n):
    fillcolor()
    for i in range(n):
        polygone(3,100)
        right(360/n)
        print(i+1)

number = int(input("Combien de faces ? "))
text = f"Je fais une figure de {number}"
decalage = 0
for i in range(len(text)): decalage -= 7
up()
goto(decalage, 140)
down()
write(text, font=("Helvetica",16,"normal"))
up()
goto(0,40)
down()
figure(number)
up()
goto(0,-200)
down()
figure(number)



mainloop()
