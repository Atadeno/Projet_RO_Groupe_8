import generation
import ordonnancement
import random

### Sélection ###

# Une liste non triée de 2N individus avec des durées différentes
# On trie d'abord les individus par ordre croissant
# On sélectionne les p meilleurs individus et les 1-p restants aléatoirement
# Renvoie une liste de taille N triée pour appariement

p = 0.8

def selection_population(population, p):
    population = sorted(population, key=lambda ordonnancement: ordonnancement.dur) # Tri par la durée totale
    n = len(population)
    selected = population[:int(p*n/2)]
    population = population[int(p*n/2):]
    random.shuffle(population) # On mélange le reste de la liste
    selected += sorted(population[:int((1-p)*n/2)+1], key=lambda ordonnancement: ordonnancement.dur) # La liste étant déjà triée, on ajoute le reste trié! 
    return selected

"""
pop = generation.generation_aleatoire("jeu2.txt, 1000)
pop = selection_population(pop,p)
"""


    