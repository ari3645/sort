from random import * 
from time import *

liste = [randint(0,10000) for i in range(10000)]

def triinsert(liste): 
    #tri par insertion
    t0 = time()
    
    for i in range(1,len(liste)):
        while i > 0 and liste[i] < liste[i-1]:
            liste[i-1],liste[i] = liste[i],liste[i-1]
            i = i-1
    
    tf = time()
    dt = tf-t0
    return(dt)

print(triinsert(liste))