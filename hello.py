import fltk

TailleFenetre_X = 800
TailleFenetre_Y = 800

fltk.cree_fenetre(TailleFenetre_X, TailleFenetre_Y)

margeX = TailleFenetre_X / 8
margeY = TailleFenetre_Y / 8

for i in range(1, 4):
    startX = i * margeX
    startY = i * margeY
    fltk.ligne(startX, startY, startX, TailleFenetre_Y - startY, epaisseur=2)
    fltk.ligne(startX, startY, TailleFenetre_X - startX, startY, epaisseur=2)
    fltk.ligne(startX, TailleFenetre_Y - startY, TailleFenetre_X - startX, TailleFenetre_Y - startY, epaisseur=2)
    fltk.ligne(TailleFenetre_X - startX, startY, TailleFenetre_X - startX, TailleFenetre_Y - startY, epaisseur=2)

fltk.ligne(margeX, 4 * margeY, 3 * margeX, 4 * margeY, epaisseur=2)
fltk.ligne(5 * margeX, 4 * margeY, 7 * margeX, 4 * margeY, epaisseur=2)
fltk.ligne(4 * margeX, margeY, 4 * margeX, 3 * margeY, epaisseur=2)
fltk.ligne(4 * margeX, 5 * margeY, 4 * margeX, 7 * margeY, epaisseur=2)

while True:
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)

    # Action dépendant du type d'événement reçu :

    if tev == 'Touche':
        print('Appui sur la touche', fltk.touche(ev))

    elif tev == "ClicDroit":
        print("Clic droit au point", (fltk.abscisse(ev), fltk.ordonnee(ev)))

    elif tev == "ClicGauche":
        print("Clic gauche au point", (fltk.abscisse(ev), fltk.ordonnee(ev)))

    elif tev == 'Quitte':  # on sort de la boucle
        break

    else:  # dans les autres cas, on ne fait rien
        pass

    fltk.mise_a_jour()

fltk.ferme_fenetre()
