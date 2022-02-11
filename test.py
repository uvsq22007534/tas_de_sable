#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq-info/l1-python
#########################################




########################### Blibliothèques #######################################"


import tkinter as tk
import random as r
import time

from pyparsing import CaselessKeyword 


########################### PARAMETRE FENETRE + VARIABLE GLOBAL #######################################"

global a,b,configbasique
a, b = 750,750

root = tk.Tk()
root.title("tas de sable")
root.geometry("1920x1080")
canvas = tk.Canvas(root, width = a, height = b,bg="grey")
txt1=tk.Text(root,height=5,width=35)
colors = ["blue","red","green","grey"]
configbasique=[[0,0,0],[0,4,0],[0,0,0]]
nbcase=35
x0=1
y0=1
taillecase=22

########################### FONCTIONS #######################################"

#Fonction générant aléatoirement une liste 2D de taille a,b (taille du canvas)
def Random():
    global configcourante
    configrandom=[]
    for i in range (a):
        configrandom.append([])

        for j in range (b):

            try:

                configrandom[i].append(r.randint(0,4))
                

            except IndexError:
                continue
          

    print("Configuration aléatoire crée : ")
    print("")

    print(printclear(configrandom))
    configcourante=configrandom
    coloration()  


def grille():
    for i in range(nbcase+1):
        canvas.create_line(x0+taillecase*i, y0,x0+taillecase*i,y0 + nbcase*taillecase)
        canvas.create_line(x0, y0+taillecase*i,x0+nbcase*taillecase ,y0+taillecase*i)

#Fonction qui définit la configuration basique comme configuration courante (et l'afffiche)
def basique():
    global configcourante

    configcourante=configbasique
    print(printclear(configcourante))


#Fonction qui affiche la configuration actuel dans le terminal !
def cfgcourante():
    print ("la configuration actuel est : ")
    print(printclear(configcourante))
    return


#Fonction qui Affiche la liste 2D sous la forme d'un carré
def printclear(liste1):
    for i in range (len(liste1)):
        print(liste1[i])
        
    return ""

#Test 1 de la distribution des grains de sables (pense a rajouter arg)
def distrib():
    print("Before")
    print(printclear(configcourante))
    
    for i in range (len(configcourante)):
        for j in range (len(configcourante[i])):

            if configcourante[i][j]>3:
                while (configcourante[i][j])>3:

                    try:    
                        configcourante[i][j]-=4
                        configcourante[i-1][j]+=1
                        configcourante[i][j-1]+=1
                        configcourante[i][j+1]+=1
                        configcourante[i+1][j]+=1
                    except IndexError:
                        continue
                    
                else:
                    continue
            
    print("After")
    print(printclear(configcourante)) 
    coloration()       
    return configcourante

#Fonction dessinant un pixel selon des coordonée i,j
def draw_pixel(i,j,color):
    canvas.create_rectangle( (i, j)*2,fill=color,outline="" )


#Fonction qui colore les pixel selon leurs valeurs 
def coloration():
    for i in range (len(configcourante)):
        for j in range (len(configcourante)):
            if configcourante[i][j]==1:
                draw_pixel(i,j,"yellow")
            elif configcourante[i][j]==0:
                draw_pixel(i,j,"black")
            elif configcourante[i][j]==2:
                draw_pixel(i,j,"green")
            elif configcourante[i][j]==3:
                draw_pixel(i,j,"blue")
            else:
                draw_pixel(i,j,"yellow")

#je sais plus ca sert a quoi j'etais fatiguer 
def launch():
    while True:
        for i in range (len(configcourante)):
            if 4 in configcourante[i]:
                    
                coloration()

        else:
            print("no")
            break

#Fonction qui permet d'obtenir une configuration sans case instable. -> configuration final 
def stabilisation():
    while True:

        for i in range(len(configcourante)):
            if max (configcourante[i])>3:
                distrib()
        
        else:
            break

    print("Fin !")   
    print(i-1," Itérations on été nécessaire pour venir a bout de ce tas de sable !") 

#Fonction qui permet d'obtenir la position en temps réel de la souris sur le canvas
def posmouse(event):
    posx,posy=event.x,event.y
    txt1.delete('1.0',"end")
    txt1.insert("end","clic detecte en x="+str(event.x) + " et y = " + str(event.y))
    return (posx,posy)



def clic(event):
    return


  

########################### BOUTONS #######################################"

exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random1 = tk.Button(root, text ="Random", command=Random)
Random1.grid(row=1,column=0)

distribution = tk.Button(root, text ="Distribution ", command=distrib)
distribution.grid(row=2,column=0)

colo = tk.Button(root, text ="Coloration", command=coloration)
colo.grid(row=3,column=0)

base  = tk.Button(root, text ="Basique", command=basique)
base.grid(row=4,column=0)


lancement=tk.Button(root, text ="Launch", command=launch)
lancement.grid(row=0,column=1)

stabi=tk.Button(root, text ="Stabilisation", command=stabilisation)
stabi.grid(row=0,column=2)

courante=tk.Button(root, text ="Courante", command=cfgcourante)
courante.grid(row=0,column=3)

affigrille=tk.Button(root, text ="grille", command=grille)
affigrille.grid(row=0,column=4)



########################### grid #######################################"
grid1=canvas.grid(row=1,column=1)
grid2=txt1.grid(row=1, column=2)

canvas.bind("<Button-1>",posmouse)
canvas.bind("<Motion>",posmouse)


########################### MAINLOOP du programme #######################################"
root.mainloop()
