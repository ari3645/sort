from random import * 
from time import *

liste = [randint(0,10000) for i in range(2957)]

def triselec(liste): 
    #tri par séléction
    t1 = process_time()
    
    for i in range(0,len(liste)-2):
        indmin = i
        for j in range(i+1,len(liste)):
            if liste[j] < liste[indmin]:
                indmin = j
        liste[i],liste[indmin] = liste[indmin],liste[i]
    
    tf2 = process_time()
    return(tf2-t1)

#print(triselec(liste))