# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from colorama import Fore
from colorama import Style

EMPTY = 2


def DecodeValeur(j):
    match j:
        case 'X':
            return 'X'
        case 2:
            return '*'
        case _:
            return NomJoueurs[j][0]


def AfficherPion(j: int | str):
    global ColorJoueurs
    if j == 'X':
        color = Fore.WHITE
    else:
        color = ColorJoueurs[j]
    Write(f"{color}{DecodeValeur(j)}{Style.RESET_ALL}")


def Write(texte):
    print(f"{texte}", end='')


systemColor = Fore.MAGENTA


def PrintPlateau():
    print("-------------------------")
    for j in range(rows).__reversed__():
        Write(f"{systemColor}{j} : {Style.RESET_ALL}")
        for i in range(cols):
            AfficherPion(plateau[i][j])
            Write(f" ")
        print("")
    Write("    ")
    for j in range(cols):
        Write(f"{systemColor}{j} {Style.RESET_ALL}")
    print("")


def ControlePosition(x: int, y: int):
    if (x < 0 or x >= cols) or (y < 0 or y >= rows):
        raise Exception(f"Les coordonnées fournies ({x},{y}) sont hors du périmètre.")
    if plateau[x][y] == 'X':
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est inaccessible")
    if plateau[x][y] != EMPTY:
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est déjà occupée")


def PoserPion(Joueur: int, x: int, y: int):
    ControlePosition(x, y)
    plateau[x][y] = Joueur
    PrintPlateau()


def ControlerJoueur(j: int, x: int, y: int):
    '''
    Contrôle que le joueur j possède un jeton sur la case (x,y)
        Parameters:
            j : numéro de joueur
            x : position x
            y : position y
    '''
    global NomJoueurs
    if plateau[x][y] != j:
        raise Exception(f"Le joueur numéro {NomJoueurs[j]} n'a pas de pion en position {x},{y}")


def PrendrePion(Joueur, x, y):
    ControlerJoueur(Joueur, x, y)
    plateau[x][y] = 'X'


def DeplacerPion(Joueur: int, xDepart: int, yDepart: int, xArrivee: int, yArrivee: int):
    PrendrePion(Joueur, xDepart, yDepart)
    PoserPion(Joueur, xArrivee, yArrivee)


def WriteError(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def CheckPlateau():
    nbr = [0, 0, 0]
    for i in range(rows):
        for j in range(cols):
            if plateau[i][j] != 'X':
                nbr[plateau[i][j]] = nbr[plateau[i][j]] + 1
    if nbr[0] < 3:
        return 0
    if nbr[1] < 3:
        return 1
    return EMPTY


def EndOfGame():
    if pions[0] == 0 and pions[1] == 0 and CheckPlateau() != EMPTY:
        print(f"Fin de partie !")
        return True
    return False


def InitPlateau7x7():
    global rows, cols, pions, plateau
    rows, cols, nbrPions = (7, 7, 9)
    pions = [nbrPions, nbrPions]
    # Initialisation du plateau 7x7 avec un X - position interdite
    plateau = [['X'] * cols for _ in range(rows)]
    # Place des cases comme dans un repère orthonormé
    Cases = [
        (0, 0), (0, 3), (0, 6),
        (1, 1), (1, 3), (1, 5),
        (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
        (4, 2), (4, 3), (4, 4),
        (5, 1), (5, 3), (5, 5),
        (6, 0), (6, 3), (6, 6),
    ]
    for i in range(rows):
        for j in range(cols):
            if (i, j) in Cases:
                plateau[i][j] = EMPTY
    PrintPlateau()


plateau: any = None
NomJoueurs = ["Alain", "Jébril"]
ColorJoueurs = [Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX]

# // Initialisation du Plateau
# TODO : Choix du plateau.
InitPlateau7x7()

joueur = 0


def GetJoueur():
    return NomJoueurs[joueur]


def GetCase():
    while True:
        try:
            x = int(input("Saisir l'abscisse x de la case : "))
            y = int(input("Saisir l'ordonnée y de la case : "))
            ControlePosition(x, y)
            break
        except Exception as exc:
            WriteError(exc)
    return x, y


while True:
    try:

        case = GetCase()

        PoserPion(joueur, case[0], case[1])
        if EndOfGame():
            break;
        joueur = (joueur + 1) % 2
        print(f"On passe au joueur {GetJoueur()}")

    except Exception as exc:
        WriteError(exc)
        break
