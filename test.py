import random as r

global configrandom


configrandom=[[],[],[]]

configcourante=[[2,2,3],[1,6,1],[3,2,1]]

for i in range (3):
        for j in range (3):
            configrandom[i].append(r.randint(0,10))

print(configrandom)
