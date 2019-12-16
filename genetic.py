
import ordonnancement
import job
import flowshop
import random

### Génération ###

N=1000

flow_shop = flowshop.Flowshop()
ordo = flow_shop.definir_par("jeu1.txt")
nb_machines=ordo.nb_machines

def generation_aleatoire():
    population_initiale=[]
    for i in range(N):
        random.shuffle(flow_shop.l_job)
        ordo=ordonnancement.Ordonnancement(nb_machines)
        ordo.ordonnancer_liste_job(flow_shop.l_job)
        while ordo in population_initiale:
            random.shuffle(flow_shop.l_job)
            ordo=ordonnancement.Ordonnancement(nb_machines)
            ordo.ordonnancer_liste_job(flow_shop.l_job)
        population_initiale.append(ordo)
    return population_initiale

pop=generation_aleatoire()
for i in range (10):
    pop[i].afficher()
