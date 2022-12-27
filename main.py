# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from colorama import Fore
from colorama import Style


def InitPlateau():
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
                plateau[i][j] = 0
            # else:
            #     arr[i][j] = 'X'
    PrintPlateau()


def AfficherPion(j: int | str):
    color = Fore.MAGENTA
    if j == 1:
        color = Fore.LIGHTBLUE_EX
    elif j == 2:
        color = Fore.LIGHTGREEN_EX
    elif j == 0:
        color = Fore.LIGHTYELLOW_EX
    elif j == 'X':
        color = Fore.WHITE
    print(f"{color}{j}{Style.RESET_ALL}", end='')


def PrintPlateau():
    print("-------------------------")
    for i in range(rows).__reversed__():
        for j in range(cols):
            AfficherPion(plateau[i][j])
            print(f" ", end='')
        print("")


def ControlePosition(x: int, y: int):
    if (x < 0 or x >= rows) or (y < 0 or y >= cols):
        raise Exception(f"Les coordonnées fournies ({x},{y}) sont hors du périmètre.")


def PoserPion(Joueur: int, x: int, y: int):
    ControlePosition(x, y)
    if plateau[x][y] == 'X':
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est inaccessible")
    if plateau[x][y] != 0:
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est déjà occupée")
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
    if plateau[x][y] != j:
        raise Exception(f"Le joueur numéro {j} n'a pas de pion en position {x},{y}")


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
    if nbr[1] < 3:
        return 1
    if nbr[2] < 3:
        return 2
    return 0


def EndOfGame():
    if pions[0] == 0 and pions[1] == 0 and CheckPlateau() != 0:
        print(f"Fin de partie !")


def InitPlateau7x7():
    global rows, cols, pions, plateau
    rows, cols, nbrPions = (7, 7, 9)
    pions = [0, nbrPions, nbrPions]
    plateau = [['X'] * cols for _ in range(rows)]


try:
    plateau: any = None
    # TODO : Choix du plateau.
    InitPlateau7x7()

    # // Initialisation du Plateau
    PrintPlateau()
    InitPlateau()

    PoserPion(1, 0, 0)
    PoserPion(2, 6, 6)
    PoserPion(2, 7, 7)
    EndOfGame()
    PoserPion(1, 6, 6)

except Exception as exc:
    WriteError(exc)
