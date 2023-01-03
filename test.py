from fltk import *

taille_fenetre = 30

rectangle(30,30,taille_fenetre-30,taille_fenetre-30)#carré

ligne(30,taille_fenetre/2,taille_fenetre-30,taille_fenetre/2)#trait horizontal
ligne(taille_fenetre/2,30,taille_fenetre/2,taille_fenetre-30)#trait vertical
ligne(30,30,taille_fenetre-30,taille_fenetre-30)#diagonale en haut à gauche vers en bas à droite
ligne(taille_fenetre-30,30,30,taille_fenetre-30)#diagonale en haut à droite vers en bas à gauche

cercle(30,30,10,remplissage="black")#cercle[0][0]
cercle(taille_fenetre/2,30,10,remplissage="black")#cercle[0][1]
cercle(taille_fenetre-30,30,10,remplissage="black")#cercle[0][2]

cercle(30,taille_fenetre/2,10,remplissage="black")#cercle[1][0]
cercle(taille_fenetre/2,taille_fenetre/2,10,remplissage="black")#cercle[1][1]
cercle(taille_fenetre-30,taille_fenetre/2,10,remplissage="black")#cercle[1][2]

cercle(30,taille_fenetre-30,10,remplissage="black")#cercle[2][0]
cercle(taille_fenetre/2,taille_fenetre-30,10,remplissage="black")#cercle[2][1]
cercle(taille_fenetre-30,taille_fenetre-30,10,remplissage="black")#cercle[2][2]
#"--------------------------dessin plateau 2----------------------------"
rectangle(30,30,taille_fenetre-30,taille_fenetre-30)#grand carré
rectangle((taille_fenetre/4)+30,(taille_fenetre/4)+30,((taille_fenetre/4)3)-30,((taille_fenetre/4)3)-30)#petit carré

ligne(taille_fenetre/2,30,taille_fenetre/2,(taille_fenetre/4)+30)#ligne en haut
ligne(30,taille_fenetre/2,(taille_fenetre/4)+30,taille_fenetre/2)#ligne à gauche
ligne(((taille_fenetre/4)3)-30,taille_fenetre/2,taille_fenetre-30,taille_fenetre/2)#ligne à droite
ligne(taille_fenetre/2,taille_fenetre-30,taille_fenetre/2,((taille_fenetre/4)3)-30)#ligne en bas

cercle(30,30,10,remplissage="black")#cercle[0][0]
cercle(taille_fenetre/2,30,10,remplissage="black")#cercle[0][1]
cercle(taille_fenetre-30,30,10,remplissage="black")#cercle[0][2]

cercle((taille_fenetre/4+30),(taille_fenetre/4)+30,10,remplissage="black")#cercle[1][1]
cercle(taille_fenetre/2,(taille_fenetre/4)+30,10,remplissage="black")#cercle[1][2]
cercle(((taille_fenetre/4)3)-30,(taille_fenetre/4)+30,10,remplissage="black")#cercle[1][3]
cercle(30,taille_fenetre/2,10,remplissage="black")#cercle[2][0]
cercle((taille_fenetre/4)+30,taille_fenetre/2,10, remplissage="black")#cercle[2][1]
cercle(((taille_fenetre/4))3-30,taille_fenetre/2, 10,remplissage="black")#cercle[2][3]
cercle(taille_fenetre-30,taille_fenetre/2,10,remplissage="black")#cercle[2][4]

cercle(((taille_fenetre/4)+30),((taille_fenetre/4)3)-30,10, remplissage="black")#cercle[3][1]
cercle(taille_fenetre/2,((taille_fenetre/4)3)-30,10,remplissage="black")#cercle[3][2]
cercle(((taille_fenetre/4)3)-30,((taille_fenetre/4)3)-30,10,remplissage="black")#cercle[3][3]

cercle(30,taille_fenetre-30,10,remplissage="black")#cercle[4][0]
cercle(taille_fenetre/2,taille_fenetre-30,10,remplissage="black")#cercle[4][2]
cercle(taille_fenetre-30,taille_fenetre-30,10,remplissage="black")#cercle[4][4]
"--------------------------dessin plateau 3----------------------------"
rectangle(30,30,taille_fenetre-30,taille_fenetre-30)#grand carré
rectangle((taille_fenetre/6)+30,(taille_fenetre/6)+30,((taille_fenetre/6)5)-30,((taille_fenetre/6)5)-30)#carré moyen
rectangle((taille_fenetre/3)+30,(taille_fenetre/3)+30,((taille_fenetre/6)4)-30,((taille_fenetre/6)4)-30)#petit carré

ligne(30,30,(taille_fenetre/3)+30,(taille_fenetre/3)+30)#ligne en haut à gauche
ligne(30,taille_fenetre/2,(taille_fenetre/3)+30,taille_fenetre/2)#ligne milieu à gauche
ligne(30, taille_fenetre-30,(taille_fenetre/3)+30,((taille_fenetre/6)4)-30)#ligne en bas à gauche
ligne(taille_fenetre/2,taille_fenetre-30,taille_fenetre/2,((taille_fenetre/6)4)-30)#ligne en bas au milieu
ligne(taille_fenetre-30,taille_fenetre-30,((taille_fenetre/6)4)-30,((taille_fenetre/6)4)-30)#ligne en bas à droite
ligne(taille_fenetre-30,taille_fenetre/2,((taille_fenetre/6)4)-30,(taille_fenetre/2))#ligne au milieu à droite
ligne(taille_fenetre-30,30,((taille_fenetre/6)4)-30,(taille_fenetre/3)+30)#ligne en haut à droite
ligne(taille_fenetre/2,30,(taille_fenetre/2),(taille_fenetre/3)+30)#ligne en haut au milieu

cercle(30, 30, 10, remplissage="black")#cercle[0][0]
cercle(taille_fenetre/2, 30, 10, remplissage="black")#cercle[0][3]
cercle(taille_fenetre-30, 30, 10, remplissage="black")#cercle[0][6]
cercle((taille_fenetre/6)+30,(taille_fenetre/6)+30,10,remplissage="black")#cercle[1][1]
cercle((taille_fenetre/2),(taille_fenetre/6)+30, 10, remplissage="black")#cercle[1][3]
cercle((((taille_fenetre/6))5)-30,(taille_fenetre/6)+30, 10, remplissage="black")#cercle[1][5]

cercle((taille_fenetre/3)+30,(taille_fenetre/3)+30, 10, remplissage="black")#cercle[2][2]
cercle(taille_fenetre/2, (taille_fenetre/3)+30, 10, remplissage="black")#cercle[2][3]
cercle(((taille_fenetre/6)4)-30, (taille_fenetre/3)+30, 10, remplissage="black")#cercle[2][4]
cercle(30,taille_fenetre/2, 10, remplissage="black")#cercle[3][0]
cercle((taille_fenetre/6)+30, taille_fenetre/2, 10, remplissage="black")#cercle[3][1]
cercle((taille_fenetre/3)+30, taille_fenetre/2, 10, remplissage="black")#cercle[3][2]
cercle(((taille_fenetre/6)4)-30, taille_fenetre/2, 10, remplissage="black")#cercle[3][4]
cercle(((taille_fenetre/6)5)-30, taille_fenetre/2, 10, remplissage="black")#cercle[3][5]
cercle(taille_fenetre-30, taille_fenetre/2, 10, remplissage="black")#cercle[3][6]

cercle((taille_fenetre/3)+30,((taille_fenetre/6)4)-30, 10, remplissage="black")#cercle[4][2]
cercle(taille_fenetre/2, ((taille_fenetre/6)4)-30, 10, remplissage="black")#cercle[4][3]
cercle(((taille_fenetre/6)4)-30, ((taille_fenetre/6)4)-30, 10, remplissage="black")#cercle[4][4]
cercle((taille_fenetre/6+30),((taille_fenetre/6)5)-30, 10, remplissage="black")#cercle[5][1]
cercle(taille_fenetre/2, ((taille_fenetre/6)5)-30, 10, remplissage="black")#cercle[5][3]
cercle(((taille_fenetre/6)5)-30,((taille_fenetre/6)5)-30, 10, remplissage="black")#cercle[5][5]

cercle(30, taille_fenetre-30, 10, remplissage="black")#cercle[6][0]
cercle(taille_fenetre/2, taille_fenetre-30, 10, remplissage="black")#cercle[6][3]
cercle(taille_fenetre-30, taille_fenetre-30, 10, remplissage="black")#cercle[6][6]