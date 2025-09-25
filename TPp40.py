# TP.40
# A

def ASCII(taille):
    print('X '*taille)
    for i in range(taille-2):
        print('X '+ '  '*(taille-2)+'X ')
    print('X '*taille)

ASCII(9)

print()
#B.1
print('X '*9)
for i in range(9-2):
    if i == 3:
        print('X '*9)
    else:
        print('X '+'  '*3+'X '+'  '*3+'X ')
print('X '*9)

print()
#B.2
def diagonale(cote):
    if cote % 2 == 0:
        return False
    print('X '*cote)
    for i in range(cote-2):
        print('X '+'  '*i+'X '+'  '*((cote-2)-i-1)+'X ')
    print('X '*cote)

diagonale(15)

print()
def origami(cote):
    space=1
    if cote % 2 == 0:
        return False
    print('X '*cote)
    for i in range(cote-2):
        x=13
        if cote < 10:

            if i < round(cote/2,0):
                print('X '+'  '*int((cote-3)-i)+'X '+'  '*i+'X ')
            else:
                print('X_'+'__'*int((cote-3)-i)+'X_'+'__'*space+'X_'+'__'*int((cote-3)-i)+'X_')
                space+=2
        else:
            while x <= cote:
                if x == cote:
                    x = True
                else:
                    x+=2
            if not x:

                if i < round(cote/2,0)-1:
                    print('X '+'  '*int((cote-3)-i)+'X '+'  '*i+'X ')
                else:
                    print('X_'+'__'*int((cote-3)-i)+'X_'+'__'*space+'X_'+'__'*int((cote-3)-i)+'X_')
                    space+=2
            else:
                if i < round(cote/2,0):
                    print('X '+'  '*int((cote-3)-i)+'X '+'  '*i+'X ')
                else:
                    print('X_'+'__'*int((cote-3)-i)+'X_'+'__'*space+'X_'+'__'*int((cote-3)-i)+'X_')
                    space+=2
    print('X '*cote)
    print()

origami(9)
origami(11)
origami(13)
origami(15)
origami(17)


