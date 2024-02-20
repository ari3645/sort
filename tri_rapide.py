def trirapide(tab):
    #tri rapide
    
    if not tab:
        return[]
    
    else: 
        pivot = tab[-1]
        petit = [x for x in tab     if x < pivot]
        grand = [x for x in tab[:-1]   if x >= pivot]
        return trirapide(petit) + [pivot] + trirapide(grand)
    
print(trirapide([5,-1,6,78,6,-9,4,2,-78,2]))