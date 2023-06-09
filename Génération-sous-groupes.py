#On cherche a lister les sous groupes d'un groupe G.

def liste_sous_groupes(G) :
    e = neutre(G)
    n = len(G)
    H0 = {e}
    Liste = [ H0 ]
    nA = 0 #Nombre de groupes dans Liste à l'étape précédente
    nB = 1 #Nombre de groupes dans Liste à l'étape actuelle
    while nA != nB : #tant que l'on continue à ajouter des sous groupes 
        for x in range(n)
            for i in range(len(Liste)) :
                if not x in L[i] :
                    if not sous_groupe_engendre(L[i] | {x} , e, G) in Liste :
                        Liste.append(sous_groupe_engendre(L[i] | {x} , e, G))
        nA = nB
        nB = len(Liste) 
    
#On construit les sous groupes en ajoutant des éléments et en considérant le groupe engendré. Complexité en O(n*n*n*n) dans le pire des cas.

def liste_sous_groupes_distingués(G) : 
    e = neutre(G)
    n = len(G)
    H0 = {e}
    Liste = [ H0 ]
    nA = 0
    nB = 1 
    while nA != nB : 
        for x in range(n)
            for i in range(len(Liste)) :
                if not x in L[i] :
                    if not sous_groupe_engendre(L[i] | {x} , e, G) in Liste and test_distingue(sous_groupe_engendre(L[i] | {x} , e, G), e, G):
                        Liste.append(sous_groupe_engendre(L[i] | {x} , e, G))
        nA = nB
        nB = len(Liste) 

#Meme code, on teste juste si le groupe que l'on considére d'ajouter est distingué.

def complete(G, H) :
    return H | {G[e,f] for x in H for y in H}

#On complète H pour le faire coincider avec son image par la loi de G.

def sous_groupe_engendre(H, e, G) :
    n = len(H)
    H = H | {e}
    K = complete(G,H)
    nk = len(K)
    while n!=nk :
        K = complete(G,K)
        n=nk
        nk=len(K)
    return K

#etant donné un set H inclus dans un groupe G d'élément neutre e, cette fonction renvoie le sous groupe de G engendré par H. Dans le pire des cas, on observe une complexité en O(n*n)

def test_distingue(H, e, G)
    elements_G = set(range(len(G)))
    for i in elements_G - H :
        j = inverse(G,i,e)
        if {G[G[y,h],x] for h in H} != H :
            return False
    return True
    
 #On teste si le sous groupe H est stable par action de conjugaison. SI oui, il est distingué et on renvoie True. Complexité en O(n*n) dans le pire des cas.
 
 def neutre(G) :
    n = len(G)
    for i in range(n) :
        if test_element_neutre(G, i) :
            return i
    return -1
    

