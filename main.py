# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def InitPlateau():

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
            #     arr[i][j] = None


def PrintPlateau():
    for i in range(rows):
        for j in range(cols):
            if plateau[i][j] == None:
                print('X', end='')
            else:
                print("{:1d}".format(plateau[i][j]), end='')
            print(" ", end='')
        print("")


rows, cols = (7, 7)

plateau = 0

plateau = [[None] * cols for _ in range(rows)]


# // Initialisation du Plateau
InitPlateau()
PrintPlateau()
