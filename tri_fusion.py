from random import * 
from time import *

liste = [randint(0,2000000) for i in range(10000)]
liste2 = list(liste)

def triFusion(liste):
    #tri par fusion
    
    if len(liste) == 1:
        return(liste)
    
    else:
        #récusrsivité pour rediviser en 2
        return (fusion(triFusion(liste[:len(liste)//2]) , triFusion(liste[len(liste)//2:])) )

    
def fusion(a,b):
    #fusion des listes
    
    i = 0
    j = 0
    liste1 = []
    
    while (i <= len(a)-1) and (j <= len(b)-1):
        
        if a[i] < b[j]:
            liste1.append(a[i])
            i = i+1
            
        else:
            liste1.append(b[j])
            j = j+1
            
    while i <= len(a)-1:
        for elem in a[i:]:
            liste1.append(elem)
            i=i+1
            
    while j <= len(b)-1:
        for elem in b[j:]:
            liste1.append(elem)
            j=j+1
    
    return(liste1)

t0 = process_time()    
liste = triFusion(liste)
tf3 = process_time()
liste3 = liste2.sort()
tf4 = process_time()
print(tf3-t0,tf4-tf3)


