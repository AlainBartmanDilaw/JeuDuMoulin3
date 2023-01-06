# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import signal
import sys
import traceback

import Communes

from Plateau7x7 import InitPlateau7x7

# import fltk

NomJoueurs = ["Alain", "Jébril"]


def signal_handler(sig, frame):
    print('Sortie du module demandée !')
    sys.exit(0)


def DecodeValeur(j: any):
    match j:
        case Communes.NOCASE:
            return Communes.NOCASE
        case 2:
            return Communes.EMPTYCASE
        case _:
            return NomJoueurs[j][0]  # Premier caractère du prénom


def AfficherPion(j: int | str):
    if j == Communes.NOCASE:
        color = Communes.colors.fg.lightgreen
    else:
        color = Communes.ColorJoueurs[j]
    Write(f"{color}{DecodeValeur(j)}")


def Write(texte):
    print(f"{texte}{Communes.colors.reset}", end='')


def CaseToXY(case):
    return case[0], case[1]


def ControlePosition(case):
    x, y = CaseToXY(case)
    if (x < 0 or x >= Communes.cols) or (y < 0 or y >= Communes.rows):
        raise Exception(f"Les coordonnées fournies ({x},{y}) sont hors du périmètre.")
    if Communes.plateau[x][y] == Communes.NOCASE:
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est inaccessible")
    if Communes.plateau[x][y] != Communes.Empty:
        raise Exception(
            f"Impossible de poser le jeton en position {x} {y} - la case est déjà occupée par le joueur {GetJoueur(Communes.plateau[x][y])}")


def PoserPion(case):
    x, y = CaseToXY(case)
    ControlePosition(case)
    Communes.plateau[x][y] = Communes.joueur


def ControlerJoueur(case):
    x, y = CaseToXY(case)
    '''
    Contrôle que le joueur possède un jeton sur la case (x,y)
        Parameters:
            j : numéro de joueur
            x : position x
            y : position y
    '''
    global NomJoueurs
    if Communes.plateau[x][y] != Communes.joueur:
        raise Exception(f"Le joueur numéro {GetJoueur()} n'a pas de pion en position {x},{y}")


def PrendrePion(case):
    x, y = CaseToXY(case)
    ControlerJoueur(case)
    Communes.plateau[x][y] = Communes.NOCASE


def DeplacerPion(caseDepart, caseArrivee):
    PrendrePion(caseDepart)
    PoserPion(caseArrivee)


def WriteError(message):
    print(f"{Communes.colors.bg.red}{Communes.colors.fg.black}{message}{Communes.colors.reset}")


def CheckPlateau():
    nbr = [0, 0, 0]
    for i in range(Communes.rows):
        for j in range(Communes.cols):
            if Communes.plateau[i][j] != Communes.NOCASE:
                nbr[Communes.plateau[i][j]] = nbr[Communes.plateau[i][j]] + 1
    if nbr[0] < 3:
        return 0
    if nbr[1] < 3:
        return 1
    return Communes.Empty


def EndOfGame():
    """
    Indique si la fin de partie est atteinte : l'un des 2 joueurs n'a plus que 2 jetons.
    :return: True si fin de partie atteinte
        False sinon
    """
    if Communes.pions[0] == 0 and Communes.pions[1] == 0 and CheckPlateau() != Communes.Empty:
        print(f"Fin de partie !")
        return True
    return False


def GetJoueur(Joueur=Communes.joueur):
    return NomJoueurs[Joueur]


def GetCase():
    while True:
        try:
            x = int(input(f"{GetJoueur()} : Saisir l'abscisse x de la case : "))
            y = int(input(f"{GetJoueur()} : Saisir l'ordonnée y de la case : "))
            ControlePosition((x, y))
            break
        except Exception as exc:
            WriteError(exc)
    return x, y


def PrintPlateau():
    print("-------------------------")
    for j in range(Communes.rows):
        Write(f"{Communes.systemColor}{j} : ")
        for i in range(Communes.cols):
            AfficherPion(Communes.plateau[i][j])
            Write(f" ")
        print("")
    Write("    ")
    for j in range(Communes.cols):
        Write(f"{Communes.systemColor}{j} ")
    print("")


signal.signal(signal.SIGINT, signal_handler)

# // Initialisation du Plateau
# TODO : Choix du plateau.
InitPlateau7x7()


def JoueurAdverse():
    return (Communes.joueur + 1) % 2


def ChangerJoueur():
    Communes.joueur = JoueurAdverse()
    print(f"On passe au joueur {GetJoueur()}")


def Tester3PionsAlignes(case):
    '''
    Fonction permettant de tester que le joueur courant ne vient pas d'aliger 3 pions
    après avoir joué son dernier pion
    :param: case = dernière case jouée
    :return: True si c'est le cas, False sinon
    '''



    return False


#
# Boucle principale interactive de test en version console
#
def SupprimerPion(adversaire):
    ok = False
    while ok != True:

        ok = True
        # Saisir la case (x,y) à supprimer
        x = y = 0
        case = (x, y)
        # Test case saisie est bien à l'adversaire
        if Communes.plateau[x][y] != adversaire:
            ok = False
            WriteError(f"Le joueur numéro {GetJoueur(adversaire)} n'a pas de pion en position {x},{y}")

        PrendrePion(case)


while True:
    try:

        case = GetCase()

        # Choix de l'action
        if Communes.pions[0] > 0 and Communes.pions[1] > 0:
            case = GetCase()
            PoserPion(case)

        if Tester3PionsAlignes(case):
            SupprimerPion(JoueurAdverse())

        if EndOfGame():
            break
        ChangerJoueur()

    except Exception as exc:
        WriteError(exc)
        WriteError(traceback.format_exc())
        break
