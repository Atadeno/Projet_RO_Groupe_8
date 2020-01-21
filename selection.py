import generation
import ordonnancement
import random

### Sélection ###

# Une liste non triée de 2N individus avec des durées différentes
# On trie d'abord les individus par ordre croissant
# On sélectionne les p meilleurs individus et les 1-p restants aléatoirement
# Renvoie une liste de taille N triée pour appariement

p = 0.8
def selection_random(population):
    random.shuffle(population)
    return population[:len(population)//2]

def selection_population_p_meilleurs(population, p):
    population = sorted(population, key=lambda ordonnancement: ordonnancement.dur) # Tri par la durée totale
    n = len(population)
    selected = population[:int(p*n/2)]
    population = population[int(p*n/2):]
    random.shuffle(population) # On mélange le reste de la liste
    selected += sorted(population[:int((1-p)*n/2)+1], key=lambda ordonnancement: ordonnancement.dur) # La liste étant déjà triée, on ajoute le reste trié! 
    return selected

def selection_population_tournoi(population, T):
    L = []
    while len(L)<(len(population)/2):
        tournoi = random.sample(population, T)
        tournoi = sorted(tournoi, key=lambda ordonnancement: ordonnancement.dur)
        L.append(tournoi[0])
    return L

def selection_population_roulette(population):
    duree = []
    for i in range(len(population)):
        duree.append(population[i].dur)
    F = sum(duree)
    cumul = 0
    cumul_duree = []
    for i in range(len(duree)):
        duree[i] = duree[i]/F
        cumul+=duree[i]
        cumul_duree.append(cumul)
    selected = []
    while len(selected)<(len(population)/2):
        p = random.random()
        i = 0
        while cumul_duree[i]<p:
            i-=-1
        selected.append(population[i])
    selected = sorted(selected, key=lambda ordonnancement: ordonnancement.dur)
    return selected 