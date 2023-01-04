import Communes


def TrouveCase(Cases, v):
    for elem in Cases:
        if elem['case'] == v:
            return elem
    return None


def InitPlateau7x7():
    Communes.rows, Communes.cols, Communes.nbrPions = (7, 7, 9)
    # Initialisation du plateau 7x7 avec un X - position interdite
    Communes.plateau = [['X'] * Communes.cols for _ in range(Communes.rows)]
    # Place des cases comme dans un repère orthonormé
    Cases = [
        # Rang 0
        {'case': (0, 0), 'voisins': ((0, 3), (3, 0))},
        {'case': (0, 3), 'voisins': ((0, 0), (1, 3), (0, 6))},
        {'case': (0, 6), 'voisins': ((0, 3), (3, 6))},
        # Rang 1
        {'case': (1, 1), 'voisins': ((3, 1), (1, 3))},
        {'case': (1, 3), 'voisins': ((1, 1), (0, 3), (2, 3), (1, 5))},
        {'case': (1, 5), 'voisins': ((1, 3), (3, 5))},
        # Rang 2
        {'case': (2, 2), 'voisins': ((3, 2), (2, 3))},
        {'case': (2, 3), 'voisins': ((2, 2), (1, 3), (2, 4))},
        {'case': (2, 4), 'voisins': ((2, 3), (3, 4))},
        # Rang 3

        {'case': (3, 0), 'voisins': ((0, 0), (6, 0), (3, 1))},
        {'case': (3, 1), 'voisins': ((3, 0), (1, 1), (5, 1), (3, 2))},
        {'case': (3, 2), 'voisins': ((3, 1), (2, 2), (4, 2))},
        {'case': (3, 4), 'voisins': ((2, 4), (4, 4), (3, 5))},
        {'case': (3, 5), 'voisins': ((3, 4), (1, 5), (5, 5), (3, 6))},
        {'case': (3, 6), 'voisins': ((3, 5), (0, 6), (6, 6))},
        # Rang 4
        {'case': (4, 2), 'voisins': ((3, 2), (4, 3))},
        {'case': (4, 3), 'voisins': ((4, 2), (5, 3), (4, 4))},
        {'case': (4, 4), 'voisins': ((4, 3), (3, 4))},
        # Rang 5
        {'case': (5, 1), 'voisins': ((3, 1), (5, 3))},
        {'case': (5, 3), 'voisins': ((5, 1), (4, 3), (6, 3), (5, 5))},
        {'case': (5, 5), 'voisins': ((5, 3), (3, 5))},
        # Rang 6
        {'case': (6, 0), 'voisins': ((3, 0), (6, 3))},
        {'case': (6, 3), 'voisins': ((6, 0), (5, 3), (6, 6))},
        {'case': (6, 6), 'voisins': ((6, 3), (3, 6))},
    ]

    ControleCases(Cases)

    for i in range(Communes.rows):
        for j in range(Communes.cols):
            value = Communes.plateau[i][j]
            elem = TrouveCase(Cases, (i, j))
            if elem != None:
                value = Communes.Empty
            Communes.plateau[i][j] = value
    Communes.pions[0] = Communes.nbrPions
    Communes.pions[1] = Communes.nbrPions


def ControleCases(Cases):
    for elem in Cases:
        case = elem['case']
        voisins = elem['voisins']
        for v in voisins:
            # print(f"{case} - {v}")
            voisins_voisins = TrouveCase(Cases, v)
            if voisins_voisins is None:
                raise Exception(f"Impossible de retrouver le voisin : {v} de la case {case}")
            else:
                if case not in voisins_voisins['voisins']:
                    raise Exception(f"La case {case} n'existe pas dans le voisin {v}")
