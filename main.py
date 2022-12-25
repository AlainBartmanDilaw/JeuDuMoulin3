# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import couleurs
from termcolor import colored, cprint
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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


print_red = lambda x: cprint(x, "red")
print_blue = lambda x: cprint(x, "blue")


def AfficherPion(j, param):
    if j == 1:
        color = Fore.BLUE
    elif j == 2:
        color = Fore.RED
    elif j == 0:
        color = Fore.WHITE
    print(f"{color}{j}{Style.RESET_ALL}", end='')


def PrintPlateau():
    print("-------------------------")
    for i in range(rows):
        for j in range(cols):
            if plateau[i][j] == 'X':
                print('X', end='')
            else:
                AfficherPion(plateau[i][j], "{:1d}".format(plateau[i][j]))
            print(f" {couleurs.couleurs.ENDC}", end='')
        print("")


def PoserPion(Joueur: int, x: int, y: int):
    if plateau[x][y] == 'X':
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est inaccessible")
    if plateau[x][y] != 0:
        raise Exception(f"Impossible de poser le jeton en position {x} {y} - la case est déjà occupée")
    plateau[x][y] = Joueur


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

try:

    rows, cols = (7, 7)
    plateau = [['X'] * cols for _ in range(rows)]

    # // Initialisation du Plateau
    PrintPlateau()
    InitPlateau()
    PrintPlateau()
    PoserPion(1, 0, 0)
    PrintPlateau()
    PoserPion(2, 6, 6)
    PrintPlateau()
    PoserPion(1, 6, 6)
    PrintPlateau()

    # colorama_init()
    # print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")
except Exception as exc:
    print(f"Exception {exc}")