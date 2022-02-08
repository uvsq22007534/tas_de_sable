#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq-info/l1-python
#########################################


#Importation des bibliothèques

from glob import glob
import tkinter as tk
import random as r


#créarion de la fenêtre + gloablisation de variable taille
global a,b,configrandom,configbasique

a, b = 500,500

root = tk.Tk()
root.title("tas de sable")
root.geometry("600x550")
canvas = tk.Canvas(root, width = a, height = b,bg="black")
colors = ["blue","red","green","grey"]
configbasique=[[0,0,0],[0,4,0],[0,0,0]]


########################### FONCTIONS #######################################"

#Fonction générant aléatoirement une liste 2D 
def Random():
    configrandom=[[],[],[]]
    for i in range (3):
        for j in range (3):
            configrandom[i].append(r.randint(0,4))
        print(configrandom[i])

#Affiche la liste 2D sous la forme d'un carré
def printclear(liste1):
    for i in range (len(liste1)):
        print(liste1[i])
        
    return ""

#Test 1 de la distribution des grains de sables (pense a rajouter arg)
def distrib():
    print("Before")
    print(printclear(configbasique))
    
    for i in range (len(configbasique)):
        for j in range (len(configbasique[i])):

            if configbasique[i][j]>3:
                while (configbasique[i][j])>3:

                    try:    
                        configbasique[i][j]-=4
                        configbasique[i-1][j]+=1
                        configbasique[i][j-1]+=1
                        configbasique[i][j+1]+=1
                        (configbasique[i+1][j])+=1
                    except IndexError:
                        continue

                else:
                    continue
            
    print("After")
    print(printclear(configbasique))        
    return ""

#Fonction dessinant un pixel
def draw_pixel(i,j,color):
    canvas.create_rectangle( (i, j)*2,fill=color,outline="" )


#Boutons
exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random1 = tk.Button(root, text ="Random", command=Random)
Random1.grid(row=4,column=0)

configbase = tk.Button(root, text ="Config base", command=distrib)
configbase.grid(row=5,column=0)


#cadrillage
grid1=canvas.grid(row=4,column=4,rowspan=1,columnspan=1)

#Test dessin d'un pixel au millieu du canvas
draw_pixel(a/2,b/2,"white")  
 
#boucle root
root.mainloop()
