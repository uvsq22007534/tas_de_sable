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
from functools import partial


########################### PARAMETRE FENETRE + VARIABLE GLOBAL #######################################"

global a,b,configbasique
a, b = 750,750

root = tk.Tk()
root.title("tas de sable")
root.geometry("1920x1080")
canvas = tk.Canvas(root, width = a, height = b,bg="white")
txt1=tk.Text(root,height=5,width=35)
configbasique=[[0,0,0],[0,4,0],[0,0,0]]
nbcase=30
x0=1
y0=1
taillecase=25
c0,c1,c2,c3,c4="grey","yellow","green","blue","purple"
it=0  
configsave=[]

########################### FONCTIONS #######################################"

#Fonction générant aléatoirement une liste 2D de taille a,b (taille du canvas)
def Random():

    global configcourante,configsave
    configrandom=[]
    for i in range (nbcase):
        configrandom.append([])

        for j in range (nbcase):

            try:

                configrandom[i].append(r.randint(0,4))
                

            except IndexError:
                continue
          

    #print("Configuration aléatoire crée : ")
    #print("")

    #print(printclear(configrandom))
    try:
        configsave=configcourante
    except NameError:
        pass


    configcourante=configrandom
    coloration()

#Fonction qui crée une liste vide et la met en configuration courante
def vide():
    global configcourante,configsave
    configvide=[]
    for i in range (nbcase):
        configvide.append([])

        for j in range (nbcase):

            try:

                configvide[i].append(0)
                

            except IndexError:
                continue
          

    #print("Configuration aléatoire crée : ")
    #print("")
    #print(printclear(configrandom)
    try:
        configsave=configcourante
    except NameError:
        pass

    configcourante=configvide
    coloration()

#Fonction qui affiche la grille 
def grille():
    for i in range(nbcase+1):
        canvas.create_line(x0+taillecase*i, y0,x0+taillecase*i,y0 + nbcase*taillecase)
        canvas.create_line(x0, y0+taillecase*i,x0+nbcase*taillecase ,y0+taillecase*i)

#Fonction qui définit la configuration basique comme configuration courante (et l'afffiche)
def basique():
    global configcourante,configsave
    configbasique=[[0,0,0],[0,4,0],[0,0,0]]
    try:
        configsave=configcourante
    except NameError:
        pass

    configcourante=configbasique
    #print(printclear(configcourante))


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
    global configsave
    #print("Before")
    #print(printclear(configcourante))
    configsave=configcourante


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
            
    #print("After")
    #print(printclear(configcourante)) 
    txt1.delete('1.0',"end")
    txt1.insert("end",it,"itération !")
    coloration()
    return configcourante




#Fonction qui colore les pixel selon leurs valeurs 
def coloration():
    global colorcarre
    colorcarre=[]
    for i in range (len(configcourante)):
        for j in range (len(configcourante[i])):
            if configcourante[i][j]==1:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill=c1))
            elif configcourante[i][j]==0:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill=c0))
            elif configcourante[i][j]==2:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill=c2))
            elif configcourante[i][j]==3:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill=c3))
            else:
                colorcarre.append(canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill=c4))

#je sais plus ca sert a quoi j'etais fatiguer 
def launch(speed):


    global colorcarre
    for i in range (len(colorcarre)):
        couleur=canvas.itemcget(colorcarre[i],'fill')
        if couleur=="purple":
       
        
            distrib()
            root.after(speed)
            root.update_idletasks()
        else:
            for j in range (len(configcourante)):
                for k in range (len(configcourante[j])):
                    if configcourante[j][k]>3:
                        distrib()
                        root.after(speed)
                        root.update_idletasks()
                    else:
                        pass

        
            
    

    


#Fonction qui permet d'obtenir une configuration sans case instable. -> configuration final 
def stabilisation():

    for i in range(len(colorcarre)):
        couleur = canvas.itemcget(i, 'fill') 
        if couleur =="purple":
            distrib()

    coloration()    
    print("il a fallu ",i," intération pour venir a bout de ce tas de sable")




#Fonction qui permet d'obtenir la position en temps réel de la souris sur le canvas
def posmouse(event):
    posx,posy=event.x,event.y
    txt1.delete('1.0',"end")
    txt1.insert("end","clic detecte en x="+str(event.x) + " et y = " + str(event.y))
    return (posx,posy)

#Fonction qui permet de colorier une case sur la quelle on clique ! (augmente la couleur avec clique gauche)
def closemouse1(event):
    global poslistx,poslisty,configcourante
    poslistx=0
    poslisty=0
    posx,posy=event.x,event.y
    objet =canvas.find_closest(posx, posy)
    couleur = canvas.itemcget(objet[0], 'fill') 
    poslisty=int(posy)//taillecase
    poslistx=int(event.x)//taillecase
    if couleur == c0:
        canvas.itemconfig(objet[0], fill=c1)
        configcourante[poslistx][poslisty]+=1
    elif couleur == c1:
        canvas.itemconfig(objet[0], fill=c2)
        configcourante[poslistx][poslisty]+=1
    elif couleur ==c2:
        canvas.itemconfig(objet[0], fill=c3)
        configcourante[poslistx][poslisty]+=1
    elif couleur == c3:
        canvas.itemconfig(objet[0], fill=c4)
        configcourante[poslistx][poslisty]+=1
    print(printclear(configcourante))
    
#Fonction qui permet de colorier une case sur la quelle on clique ! (décroit avec le clique droit)   
def closemouse2(event):
    global poslistx,poslisty
    poslistx=0
    poslisty=0
    posx,posy=event.x,event.y
    objet =canvas.find_closest(posx, posy)
    couleur = canvas.itemcget(objet[0], 'fill')
    poslisty=int(posy)//taillecase
    poslistx=int(event.x)//taillecase

    if couleur == c4:
        canvas.itemconfig(objet[0], fill=c3)
        configcourante[poslistx][poslisty]-=1
    elif couleur == c3:
        canvas.itemconfig(objet[0], fill=c2)
        configcourante[poslistx][poslisty]-=1
    elif couleur ==c2:
        canvas.itemconfig(objet[0], fill=c1)
        configcourante[poslistx][poslisty]-=1
    elif couleur == c1:
        canvas.itemconfig(objet[0], fill=c0)
        configcourante[poslistx][poslisty]-=1



def popup():
    win = tk.Toplevel()
    win.wm_title("Choix du temps d'itération")
    win.geometry("800x200")
    l200=200
    l500=500
    l1000=1000
    l5000=5000
    l = tk.Label(win, text="Choisissez un temps entre chaque itération !")
    l.configure(font=("Comic", 15,))
    l.grid(row=0, column=2)

    b = tk.Button(win, text="0.2 seconde", command=partial(launch,(l200)))
    b.grid(row=3, column=1)

    c = tk.Button(win, text="0.5 seconde", command=partial(launch,(l500)))
    c.grid(row=3, column=2)

    d = tk.Button(win, text="1 seconde", command=partial(launch,(l1000)))
    d.grid(row=3,column=3)

    e = tk.Button(win, text="5 secondes", command=partial(launch,(l5000)))
    e.grid(row=3, column=4)

def undo():
    global configcourante
    configcourante=configsave
    print(configsave)
    coloration()

def save():
 
    # Enregistre ta liste dans ton fichier.txt
    with open('fichier.txt', 'w') as f:
        for item in configcourante:
            f.write(f'{item}\n')



########################### BOUTONS #######################################"

exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random1 = tk.Button(root, text ="Random", command=Random)
Random1.grid(row=2,column=0)

distribution = tk.Button(root, text ="Distribution ", command=distrib)
distribution.grid(row=1,column=0)

colo = tk.Button(root, text ="Coloration", command=coloration)
colo.grid(row=3,column=0)

base  = tk.Button(root, text ="Basique", command=basique)
base.grid(row=4,column=0)


pop=tk.Button(root, text ="LAUNCH", command=popup)
pop.grid(row=0,column=1)

stabi=tk.Button(root, text ="Stabilisation", command=stabilisation)
stabi.grid(row=0,column=2)

courante=tk.Button(root, text ="Courante", command=cfgcourante)
courante.grid(row=0,column=3)

affigrille=tk.Button(root, text ="grille", command=grille)
affigrille.grid(row=0,column=4)

cfgvide=tk.Button(root, text ="Vide", command=vide)
cfgvide.grid(row=0,column=5)

undob=tk.Button(root, text ="Undo", command=undo)
undob.grid(row=0,column=6)

save=tk.Button(root, text ="Save", command=save)
save.grid(row=5,column=0)




########################### grid #######################################"
grid1=canvas.grid(row=1,column=1)
grid2=txt1.grid(row=1, column=2)

########################### bind #######################################"
canvas.bind("<Button-1>",closemouse1)
canvas.bind("<Motion>",posmouse)
canvas.bind("<Button-3>",closemouse2)

########################### MAINLOOP du programme #######################################"
root.mainloop()
