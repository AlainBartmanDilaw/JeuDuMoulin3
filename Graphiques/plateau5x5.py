from fltk import *

taille_fenetre = 600
cree_fenetre(taille_fenetre, taille_fenetre)

# --------------------------dessin plateau 2----------------------------#
image(taille_fenetre / 2, taille_fenetre / 2, r'..\Ressources\background.pgm', ancrage='center')

rectangle(30, 30, taille_fenetre - 30, taille_fenetre - 30, remplissage="beige")  # grand carré
rectangle((taille_fenetre / 4) + 30, (taille_fenetre / 4) + 30, ((taille_fenetre / 4) * 3) - 30,
          ((taille_fenetre / 4) * 3) - 30, remplissage="beige")  # petit carré

ligne(taille_fenetre / 2, 30, taille_fenetre / 2, (taille_fenetre / 4) + 30)  # ligne en haut
ligne(30, taille_fenetre / 2, (taille_fenetre / 4) + 30, taille_fenetre / 2)  # ligne à gauche
ligne(((taille_fenetre / 4) * 3) - 30, taille_fenetre / 2, taille_fenetre - 30, taille_fenetre / 2)  # ligne à droite
ligne(taille_fenetre / 2, taille_fenetre - 30, taille_fenetre / 2, ((taille_fenetre / 4) * 3) - 30)  # ligne en bas

cercle(30, 30, 10, remplissage="black")  # cercle[0][0]
cercle(taille_fenetre / 2, 30, 10, remplissage="black")  # cercle[0][1]
cercle(taille_fenetre - 30, 30, 10, remplissage="black")  # cercle[0][2]

cercle(((taille_fenetre / 4) + 30), (taille_fenetre / 4) + 30, 10, remplissage="black")  # cercle[1][1]
cercle(taille_fenetre / 2, (taille_fenetre / 4) + 30, 10, remplissage="black")  # cercle[1][2]
cercle(((taille_fenetre / 4) * 3) - 30, (taille_fenetre / 4) + 30, 10, remplissage="black")  # cercle[1][3]

cercle(30, taille_fenetre / 2, 10, remplissage="black")  # cercle[2][0]
cercle((taille_fenetre / 4) + 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[2][1]
cercle((((taille_fenetre / 4)) * 3) - 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[2][3]
cercle(taille_fenetre - 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[2][4]

cercle(((taille_fenetre / 4) + 30), ((taille_fenetre / 4) * 3) - 30, 10, remplissage="black")  # cercle[3][1]
cercle(taille_fenetre / 2, ((taille_fenetre / 4) * 3) - 30, 10, remplissage="black")  # cercle[3][2]
cercle(((taille_fenetre / 4) * 3) - 30, ((taille_fenetre / 4) * 3) - 30, 10, remplissage="black")  # cercle[3][3]

cercle(30, taille_fenetre - 30, 10, remplissage="black")  # cercle[4][0]
cercle(taille_fenetre / 2, taille_fenetre - 30, 10, remplissage="black")  # cercle[4][2]
cercle(taille_fenetre - 30, taille_fenetre - 30, 10, remplissage="black")  # cercle[4][4]

# --------------------------boutons plateau 2------------------------#


while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":

        if 20 <= abscisse(ev) <= 40 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][0]
            cercle(30, 30, 10, remplissage="yellow")
        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][1]
            cercle(taille_fenetre / 2, 30, 10, remplissage="yellow")

        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][2]
            cercle(taille_fenetre - 30, 30, 10, remplissage="yellow")


        elif (taille_fenetre / 4) + 20 <= abscisse(ev) <= (taille_fenetre / 4) + 40 and (
                taille_fenetre / 4) + 20 <= ordonnee(ev) <= (taille_fenetre / 4) + 40:
            # action cercle[1][1]
            cercle(((taille_fenetre / 4) + 30), (taille_fenetre / 4) + 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                taille_fenetre / 4) + 20 <= ordonnee(ev) <= (taille_fenetre / 4) + 40:
            # action cercle[1][2]
            cercle(taille_fenetre / 2, (taille_fenetre / 4) + 30, 10, remplissage="yellow")

        elif ((taille_fenetre / 4) * 3) - 40 <= abscisse(ev) <= ((taille_fenetre / 4) * 3) - 20 and (
                taille_fenetre / 4) + 20 <= ordonnee(ev) <= (taille_fenetre / 4) + 40:
            # action cercle[1][3]
            cercle(((taille_fenetre / 4) * 3) - 30, (taille_fenetre / 4) + 30, 10, remplissage="yellow")


        elif 20 <= abscisse(ev) <= 40 and (taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[2][0]
            cercle(30, taille_fenetre / 2, 10, remplissage="yellow")

        elif (taille_fenetre / 4) + 20 <= abscisse(ev) <= (taille_fenetre / 4) + 40 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[2][1]
            cercle((taille_fenetre / 4) + 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif (((taille_fenetre / 4)) * 3) - 40 <= abscisse(ev) <= (((taille_fenetre / 4)) * 3) - 20 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[2][3]
            cercle((((taille_fenetre / 4)) * 3) - 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and (taille_fenetre / 2) - 10 <= ordonnee(
                ev) <= (taille_fenetre / 2) + 10:
            # action cercle[2][4]
            cercle(taille_fenetre - 30, taille_fenetre / 2, 10, remplissage="yellow")


        elif ((taille_fenetre / 4) + 20) <= abscisse(ev) <= ((taille_fenetre / 4) + 40) and (
                (taille_fenetre / 4) * 3) - 40 <= ordonnee(ev) <= ((taille_fenetre / 4) * 3) - 20:
            # action cercle[3][1]
            cercle(((taille_fenetre / 4) + 30), ((taille_fenetre / 4) * 3) - 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                (taille_fenetre / 4) * 3) - 40 <= ordonnee(ev) <= ((taille_fenetre / 4) * 3) - 20:
            # action cercle[3][2]
            cercle(taille_fenetre / 2, ((taille_fenetre / 4) * 3) - 30, 10, remplissage="yellow")

        elif ((taille_fenetre / 4) * 3) - 40 <= abscisse(ev) <= ((taille_fenetre / 4) * 3) - 20 and (
                (taille_fenetre / 4) * 3) - 40 <= ordonnee(ev) <= ((taille_fenetre / 4) * 3) - 20:
            # action cercle[3][3]
            cercle(((taille_fenetre / 4) * 3) - 30, ((taille_fenetre / 4) * 3) - 30, 10, remplissage="yellow")

        elif 20 <= abscisse(ev) <= 40 and taille_fenetre - 40 <= ordonnee(ev) <= taille_fenetre - 20:
            # action cercle[4][0]
            cercle(30, taille_fenetre - 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and taille_fenetre - 40 <= ordonnee(
                ev) <= taille_fenetre - 20:
            # action cercle[4][2]
            cercle(taille_fenetre / 2, taille_fenetre - 30, 10, remplissage="yellow")

        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and taille_fenetre - 40 <= ordonnee(
                ev) <= taille_fenetre - 20:
            # action cercle[4][4]
            cercle(taille_fenetre - 30, taille_fenetre - 30, 10, remplissage="yellow")



    else:  # dans les autres cas, on ne fait rien
        pass

    mise_a_jour()

ferme_fenetre()
