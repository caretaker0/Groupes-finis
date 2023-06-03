import numpy as np

#Pour representer un groupe, on utilise un tableau incarnant la table de la loi du groupe.
#On cherche a ecrire une fonction qui vérifie, étant donné une table de loi, si cette table est celle d'un groupe.

def test_groupe(G) :
    n = len(G)
    e = element_neutre(G)
    if test_associativite(G) :
        if e != -1 :
            for j in range(n) :
                if inverse(G, j, e) == -1 :
                    return False
            return True
        return False 

#Cette fonction teste si la loi G est celle d'un groupe avec une complxité en O(n*n*n) (test d'associativité). Si G represente un groupe, elle renvoie True et renvoie False sinon. 

#Avec les sous fonctions suivantes :

def test_associativite(G) :
    n = len(G)
    for i in range(n) :
        for j in range(n):
            for k in range(n) :
                if G[ G[i,j], k] != G[ i, G[j,k]] :
                    return False
    return True

#Cette fonction vérifie si la loi de G est associative. On verifie simplement si la propriété "pour tous x y z (xy)z = x(yz) est vraie. Complexité en O(n*n*n).

def test_commutativite(G) :
    n = len(G)
    for i in range(n) :
        for j in range(n) :
            if G[i,j] != G[j,i] :
                return False
    return True
   
#Cette fonction vérifie si la loi de G est commutative. On verifie simplement si la table de loi est symétrique par rapport à la diagonale. Complexité en O(n*n).

 def test_element_neutre(G, e) :
    n = len(G)
    for i in range(n) :
        if G[x,e] != x or G[e,x] != x :
            return False
    return True
    
#Cette fonction vérifie, étant donné e dans G, si G est neutre pour la loi de G. Complexité en O(n)

def element_neutre(G) :
    n = len(G)
    for i in range(n) :
        if test_element_neutre(G, i) :
            return i
    return -1
    
#Cette fonction cherche parmi tout les éléments de G si l'un d'entre eux est neutre pour la loi de G, et renvoie le premier qu'elle croise. Si elle n'en trouve aucun, la fonction renvoie -1. Complexité en O(n).

def inverse(G, x, e) :
    n = len(G)
    for j in range(n) :
        if G[x,y] = e and G[y,x] = e :
            return y 
    return -1
    
#Cette fonction prend en entrée une table G, un élément x et un élément neutre e et cherche un symétrique de x pour la loi G par e. Complexité en O(n)
