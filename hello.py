# import sys
from fltk import *
#
# window = Fl_Window(300,180)
# box = Fl_Box(20,40,260,100,"Hello, World!")
# box.box(FL_UP_BOX)
# box.labelsize(36)
# box.labelfont(FL_BOLD+FL_ITALIC)
# box.labeltype(FL_SHADOW_LABEL)
# window.end()
# window.show(sys.argv)
# Fl.run()

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