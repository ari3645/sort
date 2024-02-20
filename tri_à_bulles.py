from random import * 
from time import *

liste = [randint(0,10000) for i in range(10000)]
def tribubble(liste): 
    #tri à bulles
    
    t0 = time()

    for b in range(len(liste)-1):
        for a in range(len(liste)-1):
            if liste[a] > liste[a+1]:
                g = liste[a]
                liste[a] = liste[a+1]
                liste[a+1] = g

    tf = time()
    dt = tf-t0
    return (dt)

#print(tribubble(liste))