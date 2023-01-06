from fltk import *

taille_fenetre = 600
cree_fenetre(taille_fenetre, taille_fenetre)

# image
image(taille_fenetre / 2, taille_fenetre / 2, r'.\Ressources\background.pgm', ancrage='center')

# titre
texte(taille_fenetre // 3, 30, "Jeu du moulin", couleur="red", taille=taille_fenetre // 20,
      police=r'Ressources/HappyMonksMedievalLookingScript.ttf')

# plateau 3 jetons
rectangle(taille_fenetre / 5, taille_fenetre / 3, taille_fenetre / 1.2, taille_fenetre / 2.5, remplissage="green")
texte(taille_fenetre / 2.4, taille_fenetre / 2.9, "plateau 1", couleur="black", taille=taille_fenetre // 30)

# plateau 6 jetons
rectangle(taille_fenetre / 5, taille_fenetre / 2, taille_fenetre / 1.2, taille_fenetre / 1.75, remplissage="blue")
texte(taille_fenetre / 2.4, taille_fenetre / 1.93, "plateau 2", couleur="black", taille=taille_fenetre // 30)

# plateau 9 jetons
rectangle(taille_fenetre / 5, taille_fenetre / 1.5, taille_fenetre / 1.2, taille_fenetre / 1.35, remplissage="orange")
texte(taille_fenetre / 2.4, taille_fenetre / 1.46, "plateau 3", couleur="black", taille=taille_fenetre // 30)

# plateau 12 jetons
rectangle(taille_fenetre / 5, taille_fenetre / 1.25, taille_fenetre / 1.2, taille_fenetre / 1.15, remplissage="red")
texte(taille_fenetre / 2.4, taille_fenetre / 1.22, "plateau 4", couleur="black", taille=taille_fenetre // 30)

# boutons
while True:
    ev = donne_ev()
    tev = type_ev(ev)

    # plateau1
    if tev == "ClicGauche":
        if taille_fenetre / 5 <= abscisse(ev) <= taille_fenetre / 1.2 and taille_fenetre / 3 <= ordonnee(
                ev) <= taille_fenetre / 2.5:
        # boutons plateau 1 choisir une action
            pass

        elif taille_fenetre / 5 <= abscisse(ev) <= taille_fenetre / 1.2 and taille_fenetre / 2 <= ordonnee(
                ev) <= taille_fenetre / 1.75:
        # boutons plateau 2 choisir une action
            pass

        elif taille_fenetre / 5 <= abscisse(ev) <= taille_fenetre / 1.2 and taille_fenetre / 1.5 <= ordonnee(
                ev) <= taille_fenetre / 1.35:
        # boutons plateau 3 choisir une action
            pass

        elif taille_fenetre / 5 <= abscisse(ev) <= taille_fenetre / 1.2 and taille_fenetre / 1.25 <= ordonnee(
            ev) <= taille_fenetre / 1.15:
    # boutons plateau 4 choisir une action
            pass

    else:  # dans les autres cas, on ne fait rien
        pass

    mise_a_jour()
ferme_fenetre()
