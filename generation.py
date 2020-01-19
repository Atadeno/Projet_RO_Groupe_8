
import ordonnancement
import job
import flowshop
import random
import numpy as np

### Génération ###

def generation_Heuristique (mon_fichier_txt, N):
    flow_shop = flowshop.Flowshop()
    ordo = flow_shop.definir_par(mon_fichier_txt) # Construction d'un problème avec un fichier .txt
    nb_machines = ordo.nb_machines
    liste_job = ordo.seq
    nbr_Jobs=len(liste_job)
    
    t=[] #processing time matrix
    for job in liste_job
        t.append(job.duree_op)
        
    palmIndex=[0 for i in range(n)] #index de pente de Palmer de chaque tache

    for i in range(1,nbr_Jobs):
        sum=0
        for j in range (1,nb_machines):
            sum=sum+(nb_machines-2*j+1)*t[i,j]
        palmIndex[i]=sum

    johnIndex=[0 for i in range(nbr_Jobs)] #index de pente de Johnson de chaque tache
    for i in range (1,nbr_Jobs):
        mi=10000
        for j in range (1,nb_machines-1):
            if t[i,j]+t[i,j+1]<mi:
                mi=t[i,j]+t[i,j+1]
        signe=1
        if (t[i,1]-t[i,nb_machines])<0:
            signe=-1
        johnIndex[i]=palmIndex[i]-signe/mi

    palmerSol=[-1 for i in range(nbr_Jobs)] #Solution basée sur indice de Palmer
    johnsonSol=[-1 for i in range(nbr_Jobs)] #Solution basée sur indice de Johnson
    for k in range (1,nbr_Jobs):
        ind=1
        while palmerSol[ind]!=-1 & palmIndex[palmerSol[ind]]<palmIndex[k]:
            ind=ind+1
        palmerSol[ind]=k   
        ind2=1
        while johnsonSol[ind]!=-1 & johnIndex[johnsonSol[ind]]<johnIndex[k]:
            ind2=ind2+1
        johnsonSol[ind2]=k

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

