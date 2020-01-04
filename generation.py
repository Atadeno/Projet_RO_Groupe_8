
import ordonnancement
import job
import flowshop
import random

### Génération ###

N = 10000 # TD Choisir N en fonction du nombre de jobs

flow_shop = flowshop.Flowshop()
ordo = flow_shop.definir_par("jeu1.txt") # Construction d'un problème avec un fichier .txt
nb_machines = ordo.nb_machines

def generation_aleatoire():
    population_initiale=[]
    i = 0
    while (i < N):
        random.shuffle(flow_shop.l_job) # Mélange des jobs
        ordo = ordonnancement.Ordonnancement(nb_machines) # Création d'un nouvel ordonnancement
        ordo.ordonnancer_liste_job(flow_shop.l_job) # Ordonnancer avec la nouvelle liste

        """
        ordo.afficher()
        population_initiale.append(ordo)
        """
        i-=-1
    return population_initiale

pop = generation_aleatoire()

# Print pour comprendre le problème de la fonction afficher()
"""
for i in range (10):
    pop[i].afficher()
"""