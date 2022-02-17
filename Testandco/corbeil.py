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


########################### PARAMETRE FENETRE + VARIABLE GLOBAL #######################################"

global a,b,configbasique
a, b = 100,100

root = tk.Tk()
root.title("tas de sable")
root.geometry("600x550")
canvas = tk.Canvas(root, width = a, height = b,bg="grey")
colors = ["blue","red","green","grey"]
configbasique=[[0,0,0],[0,4,0],[0,0,0]]


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

#je sais plus ca sert a quoi j'etait fatiguer 
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



########################### BOUTONS #######################################"

exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random1 = tk.Button(root, text ="Random", command=Random)
Random1.grid(row=4,column=0)

distribution = tk.Button(root, text ="Distribution ", command=distrib)
distribution.grid(row=5,column=0)

colo = tk.Button(root, text ="Coloration", command=coloration)
colo.grid(row=6,column=0)

base  = tk.Button(root, text ="Basique", command=basique)
base.grid(row=7,column=0)


lancement=tk.Button(root, text ="Launch", command=launch)
lancement.grid(row=0,column=1)

stabi=tk.Button(root, text ="Stabilisation", command=stabilisation)
stabi.grid(row=0,column=2)

courante=tk.Button(root, text ="Courante", command=cfgcourante)
courante.grid(row=0,column=3)




########################### grid #######################################"
grid1=canvas.grid(row=10,column=4,rowspan=10,columnspan=10)



########################### MAINLOOP du programme #######################################"
root.mainloop()



f couleur == c0:
        canvas.itemconfig(objet[0], fill=c1)
        configcourante[poslistx-1][poslisty-1]+1
    elif couleur == c1:
        canvas.itemconfig(objet[0], fill=c2)
        configcourante[poslistx-1][poslisty-1]+1
    elif couleur ==c2:
        canvas.itemconfig(objet[0], fill=c3)
        configcourante[poslistx-1][poslisty-1]+1
    elif couleur == c3:
        canvas.itemconfig(objet[0], fill=c4)
        configcourante[poslistx-1][poslisty-1]+1
def stabilisation():
    while True:
        print()
        for i in range(len(configcourante)):
            for j in range (len(configcourante[i])):
                cfgc=configcourante[i][j]
                if configcourante.count(cfgc>3):
                    distrib()
                    time.sleep(1)
                    coloration()
        break


  global colorcarre
    for i in range (len(colorcarre)):
        couleur=canvas.itemcget(colorcarre[i],'fill')
        if couleur=="purple":
        
            distrib()
            root.after(500)
            root.update_idletasks()
    