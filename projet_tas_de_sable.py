#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq-info/l1-python
#########################################


#Importation des bibliothèques

import tkinter as tk

#créarion de la fenêtre + gloablisation de variable taille
global a,b
a, b = 256, 256
root = tk.Tk()
root.title("tas_de_sable")
root.geometry("100x100")
canvas = tk.Canvas(root, width = a, height = b,bg="black")



#boucle root
root.mainloop()
