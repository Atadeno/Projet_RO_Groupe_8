import generation
import ordonnancement
import random

### Mutation ###

# Une liste de 2N individus dont les N derniers sont les fils
# On réalise une mutation à 10% sur les enfants
# Une mutation est un échange entre 2 jobs

def muter(ordo_initial):
    n = len(ordo_initial.seq)
    i = random.randint(0,n-1) # Dans le pire des cas, on ne fait pas d'échange!
    j = random.randint(0,n-1)
    ordo_initial.seq[i], ordo_initial.seq[j] = ordo_initial.seq[j], ordo_initial.seq[i]
    ordo = ordonnancement.Ordonnancement(ordo_initial.nb_machines) # Création d'un nouvel ordonnancement
    ordo.ordonnancer_liste_job(ordo_initial.seq)
    return ordo
    
def mutation_population(population, pourcentage):
    N = len(population)//2
    for i in range(N,2*N):
        p = random.randint(1,100)
        if (p <= pourcentage): # Probabilité de mutation: pourcentage%
            population[i] = muter(population[i])

"""
pop = generation.generation_aleatoire("jeu2.txt", 1000)
mutation_population(pop)
"""