
import ordonnancement
import job
import flowshop
import random

### Génération ###

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

N = 1000 # TD Choisir N en fonction du nombre de jobs, N est pair
pop = generation_aleatoire("jeu2.txt", N)

"""
for i in range (10):
    pop[i].afficher()
"""