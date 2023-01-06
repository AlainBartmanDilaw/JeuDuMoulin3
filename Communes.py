from colors import colors

Empty = 2
plateau = []

rows, cols, nbrPions = (0, 0, 0)

pions = [0, 0]

# NOCASE = '\u220e'
# NOCASE = '\u2981'
NOCASE = '+'

EMPTYCASE = 'x'
# EMPTYCASE = '\u00f8'


joueur = 0

ColorJoueurs = [colors.fg.black + colors.bg.cyan, # Joueur 1
                colors.fg.black + colors.bg.orange, # Joueur 2
                colors.fg.pink # Case vide
                ]
systemColor = colors.fg.cyan

DonneesPlateau = []

Moulins = []

NomJoueurs = ["1er Joueur", "2eme Joueur"]
