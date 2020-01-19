
import ordonnancement
import job
import flowshop
import random
import numpy as np

### Génération ###

def generation_Heuristique(mon_fichier_txt, N):
    flow_shop = flowshop.Flowshop()
    ordo = flow_shop.definir_par(mon_fichier_txt) # Construction d'un probleme avec un fichier .txt
    nb_machines = ordo.nb_machines
    liste_job = ordo.seq
    nbr_Jobs=len(liste_job)
    
    #t=[[5,9,8,10,1],[9,3,10,1,8],[9,4,5,8,6],[4,8,8,7,2]] #processing time matrix
    #nbr_Jobs=4
    #nb_machines=5
    for job in liste_job:
        t.append(job.duree_op)
        
    palmIndex=[0 for i in range(nbr_Jobs)] #index de pente de Palmer de chaque tache

    for i in range(nbr_Jobs):
        sum=0
        for j in range (nb_machines):
            sum=sum+(nb_machines-2*j+1)*t[i][j]
        palmIndex[i]=sum

    johnIndex=[0 for i in range(nbr_Jobs)] #index de pente de Johnson de chaque tache
    for i in range (nbr_Jobs):
        mi=10000
        for j in range (nb_machines-1):
            if t[i][j]+t[i][j+1]<mi:
                mi=t[i][j]+t[i][j+1]
        signe=1
        if (t[i][1]-t[i][nb_machines-1])<0:
            signe=-1
        johnIndex[i]=palmIndex[i]-signe/mi

    palmerSol=[0] #Solution basee sur indice de Palmer
    johnsonSol=[0] #Solution basee sur indice de Johnson
    for k in range (1,nbr_Jobs):
        ind=0
        while (ind<len(palmerSol) & palmIndex[palmerSol[ind]]<palmIndex[k]):
            ind+=1
        palmerSol.insert(ind,k)
    
    for n in range(1,nbr_Jobs):
        ind2=0
        while (ind2<len(johnsonSol) & johnIndex[johnsonSol[ind2]]<johnIndex[k]):
            ind2+=1
        johnsonSol.insert(ind2,n)

    return(palmerSol,johnsonSol)
    


def generation_aleatoire(mon_fichier_txt, N):

    flow_shop = flowshop.Flowshop()
    ordo = flow_shop.definir_par(mon_fichier_txt) # Construction d'un problème avec un fichier .txt
    nb_machines = ordo.nb_machines
    liste_job = ordo.seq

    population_initiale=[]
    i = 0
    while (i < N):
        random.shuffle(liste_job) # Mélange des jobs
        ordo_new = ordonnancement.Ordonnancement(nb_machines) # Création d'un nouvel ordonnancement
        ordo_new.ordonnancer_liste_job(liste_job) # Ordonnancer avec la nouvelle liste
        population_initiale.append(ordo_new)
        i-=-1
    return population_initiale

pop = generation_Heuristique("jeu1.txt",2)
