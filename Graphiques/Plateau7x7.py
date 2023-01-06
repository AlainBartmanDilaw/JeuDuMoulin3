from fltk import *

taille_fenetre = 600
cree_fenetre(taille_fenetre, taille_fenetre)

"--------------------------dessin plateau 4----------------------------"
image(taille_fenetre / 2, taille_fenetre / 2, r'..\Ressources\background.pgm', ancrage='center')
rectangle(30, 30, taille_fenetre - 30, taille_fenetre - 30, remplissage="beige")  # grand carré
rectangle((taille_fenetre / 6) + 30, (taille_fenetre / 6) + 30, ((taille_fenetre / 6) * 5) - 30,
          ((taille_fenetre / 6) * 5) - 30)  # carré moyen
rectangle((taille_fenetre / 3) + 30, (taille_fenetre / 3) + 30, ((taille_fenetre / 6) * 4) - 30,
          ((taille_fenetre / 6) * 4) - 30)  # petit carré

ligne(30, 30, (taille_fenetre / 3) + 30, (taille_fenetre / 3) + 30)  # ligne en haut à gauche
ligne(30, taille_fenetre / 2, (taille_fenetre / 3) + 30, taille_fenetre / 2)  # ligne milieu à gauche
ligne(30, taille_fenetre - 30, (taille_fenetre / 3) + 30, ((taille_fenetre / 6) * 4) - 30)  # ligne en bas à gauche
ligne(taille_fenetre / 2, taille_fenetre - 30, taille_fenetre / 2,
      ((taille_fenetre / 6) * 4) - 30)  # ligne en bas au milieu
ligne(taille_fenetre - 30, taille_fenetre - 30, ((taille_fenetre / 6) * 4) - 30,
      ((taille_fenetre / 6) * 4) - 30)  # ligne en bas à droite
ligne(taille_fenetre - 30, taille_fenetre / 2, ((taille_fenetre / 6) * 4) - 30,
      (taille_fenetre / 2))  # ligne au milieu à droite
ligne(taille_fenetre - 30, 30, ((taille_fenetre / 6) * 4) - 30, (taille_fenetre / 3) + 30)  # ligne en haut à droite
ligne(taille_fenetre / 2, 30, (taille_fenetre / 2), (taille_fenetre / 3) + 30)  # ligne en haut au milieu

cercle(30, 30, 10, remplissage="black")  # cercle[0][0]
cercle(taille_fenetre / 2, 30, 10, remplissage="black")  # cercle[0][3]
cercle(taille_fenetre - 30, 30, 10, remplissage="black")  # cercle[0][6]

cercle((taille_fenetre / 6) + 30, (taille_fenetre / 6) + 30, 10, remplissage="black")  # cercle[1][1]
cercle((taille_fenetre / 2), (taille_fenetre / 6) + 30, 10, remplissage="black")  # cercle[1][3]
cercle((((taille_fenetre / 6)) * 5) - 30, (taille_fenetre / 6) + 30, 10, remplissage="black")  # cercle[1][5]

cercle((taille_fenetre / 3) + 30, (taille_fenetre / 3) + 30, 10, remplissage="black")  # cercle[2][2]
cercle(taille_fenetre / 2, (taille_fenetre / 3) + 30, 10, remplissage="black")  # cercle[2][3]
cercle(((taille_fenetre / 6) * 4) - 30, (taille_fenetre / 3) + 30, 10, remplissage="black")  # cercle[2][4]

cercle(30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][0]
cercle((taille_fenetre / 6) + 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][1]
cercle((taille_fenetre / 3) + 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][2]
cercle(((taille_fenetre / 6) * 4) - 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][4]
cercle(((taille_fenetre / 6) * 5) - 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][5]
cercle(taille_fenetre - 30, taille_fenetre / 2, 10, remplissage="black")  # cercle[3][6]

cercle((taille_fenetre / 3) + 30, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="black")  # cercle[4][2]
cercle(taille_fenetre / 2, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="black")  # cercle[4][3]
cercle(((taille_fenetre / 6) * 4) - 30, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="black")  # cercle[4][4]

cercle(((taille_fenetre / 6) + 30), ((taille_fenetre / 6) * 5) - 30, 10, remplissage="black")  # cercle[5][1]
cercle(taille_fenetre / 2, ((taille_fenetre / 6) * 5) - 30, 10, remplissage="black")  # cercle[5][3]
cercle(((taille_fenetre / 6) * 5) - 30, ((taille_fenetre / 6) * 5) - 30, 10, remplissage="black")  # cercle[5][5]

cercle(30, taille_fenetre - 30, 10, remplissage="black")  # cercle[6][0]
cercle(taille_fenetre / 2, taille_fenetre - 30, 10, remplissage="black")  # cercle[6][3]
cercle(taille_fenetre - 30, taille_fenetre - 30, 10, remplissage="black")  # cercle[6][6]

"""---------------------------------------boutons plateau 4------------------------------------------"""
while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":

        if 20 <= abscisse(ev) <= 40 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][0]
            cercle(30, 30, 10, remplissage="yellow")
        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][3]
            cercle(taille_fenetre / 2, 30, 10, remplissage="yellow")
        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and 20 <= ordonnee(ev) <= 40:
            # action cercle[0][6]
            cercle(taille_fenetre - 30, 30, 10, remplissage="yellow")

        elif (taille_fenetre / 6) + 20 <= abscisse(ev) <= (taille_fenetre / 6) + 40 and (
                taille_fenetre / 6) + 20 <= ordonnee(ev) <= (taille_fenetre / 6) + 40:
            # action cercle[1][1]
            cercle((taille_fenetre / 6) + 30, (taille_fenetre / 6) + 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                taille_fenetre / 6) + 20 <= ordonnee(ev) <= (taille_fenetre / 6) + 40:
            # action cercle[1][3]
            cercle((taille_fenetre / 2), (taille_fenetre / 6) + 30, 10, remplissage="yellow")

        elif (((taille_fenetre / 6)) * 5) - 40 <= abscisse(ev) <= (((taille_fenetre / 6)) * 5) - 20 and (
                taille_fenetre / 6) + 20 <= ordonnee(ev) <= (taille_fenetre / 6) + 40:
            # action cercle[1][5]
            cercle((((taille_fenetre / 6)) * 5) - 30, (taille_fenetre / 6) + 30, 10, remplissage="yellow")


        elif (taille_fenetre / 3) + 20 <= abscisse(ev) <= (taille_fenetre / 3) + 40 and (
                taille_fenetre / 3) + 20 <= ordonnee(ev) <= (taille_fenetre / 3) + 40:
            # action cercle[2][2]
            cercle((taille_fenetre / 3) + 30, (taille_fenetre / 3) + 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                taille_fenetre / 3) + 20 <= ordonnee(ev) <= ((taille_fenetre / 3) + 40):
            # action cercle[2][3]
            cercle(taille_fenetre / 2, (taille_fenetre / 3) + 30, 10, remplissage="yellow")

        elif ((taille_fenetre / 6) * 4) - 40 <= abscisse(ev) <= ((taille_fenetre / 6) * 4) - 20 and (
                taille_fenetre / 3) + 20 <= ordonnee(ev) <= (taille_fenetre / 3) + 40:
            # action cercle[2][4]
            cercle(((taille_fenetre / 6) * 4) - 30, (taille_fenetre / 3) + 30, 10, remplissage="yellow")


        elif 20 <= abscisse(ev) <= 40 and (taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][0]
            cercle(30, taille_fenetre / 2, 10, remplissage="yellow")

        elif (taille_fenetre / 6) + 20 <= abscisse(ev) <= (taille_fenetre / 6) + 40 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][1]
            cercle((taille_fenetre / 6) + 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif (taille_fenetre / 3) + 20 <= abscisse(ev) <= (taille_fenetre / 3) + 40 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][2]
            cercle((taille_fenetre / 3) + 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif ((taille_fenetre / 6) * 4) - 40 <= abscisse(ev) <= ((taille_fenetre / 6) * 4) - 20 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][4]
            cercle(((taille_fenetre / 6) * 4) - 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif ((taille_fenetre / 6) * 5) - 40 <= abscisse(ev) <= ((taille_fenetre / 6) * 5) - 20 and (
                taille_fenetre / 2) - 10 <= ordonnee(ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][5]
            cercle(((taille_fenetre / 6) * 5) - 30, taille_fenetre / 2, 10, remplissage="yellow")

        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and (taille_fenetre / 2) - 10 <= ordonnee(
                ev) <= (taille_fenetre / 2) + 10:
            # action cercle[3][6]
            cercle(taille_fenetre - 30, taille_fenetre / 2, 10, remplissage="yellow")


        elif (taille_fenetre / 3) + 20 <= abscisse(ev) <= (taille_fenetre / 3) + 40 and (
                (taille_fenetre / 6) * 4) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 4) - 20:
            # action cercle[4][2]
            cercle((taille_fenetre / 3) + 30, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                (taille_fenetre / 6) * 4) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 4) - 20:
            # action cercle[4][3]
            cercle(taille_fenetre / 2, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="yellow")

        elif ((taille_fenetre / 6) * 4) - 40 <= abscisse(ev) <= ((taille_fenetre / 6) * 4) - 20 and (
                (taille_fenetre / 6) * 4) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 4) - 20:
            # action cercle[4][4]
            cercle(((taille_fenetre / 6) * 4) - 30, ((taille_fenetre / 6) * 4) - 30, 10, remplissage="yellow")


        elif ((taille_fenetre / 6) + 20) <= abscisse(ev) <= ((taille_fenetre / 6) + 40) and (
                (taille_fenetre / 6) * 5) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 5) - 20:
            # action cercle[5][1]
            cercle(((taille_fenetre / 6) + 30), ((taille_fenetre / 6) * 5) - 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and (
                (taille_fenetre / 6) * 5) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 5) - 20:
            # action cercle[5][3]
            cercle(taille_fenetre / 2, ((taille_fenetre / 6) * 5) - 30, 10, remplissage="yellow")

        elif ((taille_fenetre / 6) * 5) - 40 <= abscisse(ev) <= ((taille_fenetre / 6) * 5) - 20 and (
                (taille_fenetre / 6) * 5) - 40 <= ordonnee(ev) <= ((taille_fenetre / 6) * 5) - 20:
            # action cercle[5][5]
            cercle(((taille_fenetre / 6) * 5) - 30, ((taille_fenetre / 6) * 5) - 30, 10, remplissage="yellow")


        elif 20 <= abscisse(ev) <= 40 and taille_fenetre - 40 <= ordonnee(ev) <= taille_fenetre - 20:
            # action cercle[6][0]
            cercle(30, taille_fenetre - 30, 10, remplissage="yellow")

        elif (taille_fenetre / 2) - 10 <= abscisse(ev) <= (taille_fenetre / 2) + 10 and taille_fenetre - 40 <= ordonnee(
                ev) <= taille_fenetre - 20:
            # action cercle[6][3]
            cercle(taille_fenetre / 2, taille_fenetre - 30, 10, remplissage="yellow")

        elif taille_fenetre - 40 <= abscisse(ev) <= taille_fenetre - 20 and taille_fenetre - 40 <= ordonnee(
                ev) <= taille_fenetre - 20:
            # action cercle[6][6]
            cercle(taille_fenetre - 30, taille_fenetre - 30, 10, remplissage="yellow")

    else:  # dans les autres cas, on ne fait rien
        pass

    mise_a_jour()
ferme_fenetre()
