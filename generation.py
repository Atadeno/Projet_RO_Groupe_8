
import ordonnancement
import job
import flowshop
import random

### Génération ###

N = 10000 # TD Choisir N en fonction du nombre de jobs, N est pair

flow_shop = flowshop.Flowshop()
ordo = flow_shop.definir_par("jeu1.txt") # Construction d'un problème avec un fichier .txt
nb_machines = ordo.nb_machines
liste_job = ordo.seq

def generation_aleatoire():
    population_initiale=[]
    i = 0
    while (i < N):
        random.shuffle(liste_job) # Mélange des jobs
        ordo_new = ordonnancement.Ordonnancement(nb_machines) # Création d'un nouvel ordonnancement
        ordo_new.ordonnancer_liste_job(liste_job) # Ordonnancer avec la nouvelle liste
        population_initiale.append(ordo_new)
        i-=-1
    return population_initiale

pop = generation_aleatoire()

"""
for i in range (10):
    pop[i].afficher()
"""