from glob import glob
import tkinter as tk
import random as r


#créarion de la fenêtre + gloablisation de variable taille
global a,b,configrandom,configbasique

a, b = 5,5

root = tk.Tk()
root.title("tas de sable")
root.geometry("600x550")
canvas = tk.Canvas(root, width = a, height = b,bg="black")
colors = ["blue","red","green","grey"]
configbasique=[[0,0,0],[0,4,0],[0,0,0]]



def Random():
    configrandom=[]
    for i in range (a):
        for j in range (b):

            try:

                configrandom[i].append(r.randint(0,4))
            except IndexError:
                continue


        print(configrandom[i])




#Boutons
exit = tk.Button(root, text ="Exit", command = root.destroy ,fg="red")
exit.grid(row=0,column=0)

Random1 = tk.Button(root, text ="Random", command=Random)
Random1.grid(row=4,column=0)

configbase = tk.Button(root, text ="Config base", command="")
configbase.grid(row=5,column=0)


#cadrillage
grid1=canvas.grid(row=4,column=4,rowspan=1,columnspan=1)

 
#boucle root
root.mainloop()
