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
global a,b
a, b = 500,500

root = tk.Tk()
root.title("tas de sable")
root.geometry("500x500")
canvas = tk.Canvas(root, width = a, height = b,bg="black")
colors = ["blue","red","green","grey"]



########################### FONCTIONS #######################################"
def Random():
    configrandom=[[],[],[]]
    for i in range (3):
        for j in range (3):
            configrandom[i].append(r.randint(0,10))
    return print(configrandom)


#Boutons
exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random = tk.Button(root, text ="Random", command=Random)
Random.grid(row=4,column=0)



#cadrillage
grid1=canvas.grid(row=4,column=4,rowspan=1,columnspan=1)


 
#boucle root
root.mainloop()
