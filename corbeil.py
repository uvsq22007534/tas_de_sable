
#Fonction du cadrillage (taille et centre)
def grid(taille,centre):
    global taille1; global centre1
    taille1=taille
    centre1=centre

#Utilise la fonction distribution pour tout le grid
def dissipation(self):
     while True:
        found = False
        for r in range(taille1):
            for c in range(taille1):
                if grid[r][c] > 3:
                    distribution(grid[r][c], r, c)
                    found = True
        if not found:
            return


def Random():
    return 



#Fonction qui distribue le sable de Un pixel a ses voisins !
def distribution():
    return
