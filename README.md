# tas_de_sable
#########################################
# groupe Bitd 3
# Rami YAMOUT
# Nel RIVART
# Morgan NOIRET
# Bertille LANOIRE
# https://github.com/uvsq22007534/tas_de_sable
#########################################

Mode d'emploi du programme :

Tout d'abord pour le bon fonctionement verifier la correcte installation des différentes bibliothèques (tkinter, random, functools)

- Le programme s'exécute depuis le fichier tas_de_sable.py

Une fois le programme lancé, plusieurs boutons et le canvas apparaissent a l'écran.
    liste et fonction des boutons et fonctionnalitées :

        Exit : ferme le programme

        axe Y :

        distribution : Lance l'algorithme 1 fois
        Random : génére un écran aléatoire (entre 1 et 4)
        coloration : colore le canvas 
        basique : génére une liste 3x3 avec 4 au millieu
        save : sauvegarde la configuration courante sous la forme d'une liste dans un fichier .txt

        axe X :

        LAUNCH : Lance l'itération de l'algo jusqu'a temps qu'il n'y ai plus de 4 ou plus !
            + Ouvre une deuxieme fenetre de selection de temps ditération
        stabilisation : Permet d'obtenir la configuration final et de l'afficher
        courante : Affiche la configuration courante dans le terminal
        grille : affiche uen grille
        vide : crée un affichage vide (notamment pour dessiner dessus)
        undo : retour en arriere 


        Fonctionnalitées :

        Clique gauche sur le canvas : + 1 sur la case cliquée
        Clique droit sur le canvas : -1 sur la case cliquée

Comment utiliser le programme ? 

Pour utiliser le programme selectionner "Vide" pour faire apparaitre un canvas de 0 ou Random pour en générer un aléatoirement.

Dessiner sur votre canvas vide (rappel : clique gauche +1, clique droit -1) possibilité de rester cliquer pour dessiner en continue; ou passer a la suite !


code couleur :
jaune : 1
vert : 2
bleu : 3
violet : 4 ou plus 

Ensuite essayez :
    distribution : une seul itération possible de cliquer plusieurs fois 
    LAUNCH : Animation de stabilisation
    Stabilisation : obtention direct de la configuration final





