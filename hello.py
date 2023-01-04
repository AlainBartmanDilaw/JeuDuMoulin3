import fltk

fltk.cree_fenetre(400, 400)
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