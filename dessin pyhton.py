import turtle
from turtle import *
from random import randint


def fond(r):
    up()
    goto(-500, -500)
    down()
    color('darkblue')
    begin_fill()
    a = 0
    while a < 4:
        forward(1000)
        left(90)
        a = a + 1

    end_fill()


def maison(cote):
    """ Doit dessiner une maison simple (carré + triangle par dessus)

    :param cote: longueur des côtés du carré et du triangle
    """
    # Compléter la fonction ici
    up()
    goto(0, 0)
    down()
    color('black', 'blue')
    begin_fill()
    a = 0
    while a < 4:
        forward(cote)
        left(-90)
        a = a + 1
        if abs(pos()) < 1:
            break

    left(60)
    forward(cote)
    right(120)
    forward(cote)

    end_fill()


def les_maison(nb_maison):
    goto(50, 300)


def etoile(diametre, rotation):  # étoile à 5 branches
    """ Doit dessiner une étoile à 5 branches de diamètre donné, en partant avec un angle donné

    :param diamètre: diamètre de l'étoile (longueur des segments)
    :param rotation: angle de départ du crayon
    """
    # Compléter la fonction ici
    color('yellow', 'yellow')
    begin_fill()
    a = 0
    left(randint(0, 100))
    while a < 5:
        forward(diametre)
        left(144)
        a = a + 1
        if abs(pos()) < 1:
            break
    end_fill()


def Ciel_Etoile(nbr_etoile):
    i = 0
    while i < nbr_etoile:
        i = i + 1
        up()
        goto(randint(-500, 500), randint(200, 300))
        down()
        etoile(60, 5)


def arbre(branche):
    angle = 30
    color('#3f1905')

    def arbre(n, longueur):
        if n == 0:
            color('green')
            forward(longueur)  # avance
            backward(longueur)  # recule
            color('#3f1905')
        else:
            width(n)
            forward(longueur / 3)  # avance
            left(angle)  # tourne vers la gauche de angle degrés
            arbre(n - 1, longueur * 2 / 3)
            right(2 * angle)  # tourne vers la droite de angle degrés
            arbre(n - 1, longueur * 2 / 3)
            left(angle)  # tourne vers la gauche de angle degrés
            backward(longueur / 3)  # recule

    hideturtle()  # cache la tortue
    up()  # lève le stylo
    right(90)  # tourne de 90 degrés vers la droite
    forward(300)  # avance de 300 pixels
    left(180)  # fait un demi-tour
    down()  # pose le stylo
    arbre(11, 700)  # exécute la macro
    showturtle()  # affiche la tortue
    mainloop()


def on_exit():
    turtle.bye()


turtle.onkeypress(on_exit, 'e')
turtle.listen()

speed(100000)
# arbre(5)
fond(5)
maison(100)
Ciel_Etoile(10)
