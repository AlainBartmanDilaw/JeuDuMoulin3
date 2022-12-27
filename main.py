# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from colorama import Fore
from colorama import Style


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
    Write(f"{color}{j}{Style.RESET_ALL}")


def Write(texte):
    print(f"{texte}", end='')

systemColor=Fore.MAGENTA
def PrintPlateau():
    print("-------------------------")
    for i in range(rows).__reversed__():
        Write(f"{systemColor}{i} : {Style.RESET_ALL}")
        for j in range(cols):
            AfficherPion(plateau[i][j])
            Write(f" ")
        print("")
    Write("    ")
    for j in range(cols):
        Write(f"{systemColor}{j} {Style.RESET_ALL}")
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
    plateau[x][y] = Joueur+1
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
        return True
    return False


def InitPlateau7x7():
    global rows, cols, pions, plateau
    rows, cols, nbrPions = (7, 7, 9)
    pions = [0, nbrPions, nbrPions]
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
                plateau[i][j] = 0
    PrintPlateau()



plateau: any = None
# // Initialisation du Plateau
# TODO : Choix du plateau.
InitPlateau7x7()

NomJoueurs = ["Joueur 1", "Joueur 2"]

joueur = 0
while True:
    try:


        PoserPion(joueur, 0, 0)
        if EndOfGame():
            break;
        joueur = (joueur + 1) % 2
        print(f"On passe au joueur {joueur}")

    except Exception as exc:
        WriteError(exc)
        break
