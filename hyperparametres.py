import generation
import appariement
import croisement
import mutation
import selection
import ordonnancement
import time
import statistics

### Algorithme Génétique ###

N = 500
p = 0.8

fichier = "tai21.txt"

f = open("test_appariement.txt", "w")
f.write('Test Differents Appariements' +'\n')
temps_max = 360 # Temps maximal d'un calcul en secondes (ici 10 minutes)

population_initiale = generation.generation_aleatoire(fichier, N) # Génération
population_initiale = sorted(population_initiale, key=lambda ordonnancement: ordonnancement.dur)

Cmin = population_initiale[0].dur # Meilleur résultat départ
Cmax = population_initiale[-1].dur # Pire résultat départ

solutions_initiales = [population_initiale[i].dur for i in range(len(population_initiale))]
Moy = statistics.mean(solutions_initiales)

f.write('Cmin: '+str(Cmin)+' '+'Cmax: '+str(Cmax)+' '+'Moyenne: '+str(Moy)+'\n')

f.write('Random: ')
meilleures_solutions_random = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    meilleure_sequence = population[0].seq

    while (time.time()-temps_initial < temps_max): 
        appariement.appariement_population(population) # Appariement aléatoire
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population(population, p) # Sélection
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
            meilleure_sequence = population[0].seq
    meilleures_solutions_random.append(C)
f.write(str(statistics.mean(meilleures_solutions_random))+'\n')

for j in range(len(meilleures_solutions_random)):
    f.write(str(meilleures_solutions_random[j])+' ')
f.write('\n')
f.write('Sorted: ')
meilleures_solutions_sorted = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    meilleure_sequence = population[0].seq

    while (time.time()-temps_initial < temps_max): 
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population(population, p) # Sélection
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
            meilleure_sequence = population[0].seq
    meilleures_solutions_sorted.append(C)
f.write(str(statistics.mean(meilleures_solutions_sorted))+'\n')

for j in range(len(meilleures_solutions_random)):
    f.write(str(meilleures_solutions_sorted[j])+' ')
f.write('\n')
f.write('Pairing: ')
meilleures_solutions_pairing = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    meilleure_sequence = population[0].seq

    while (time.time()-temps_initial < temps_max): 
        appariement.pairing(population) # Appariement aléatoire
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population(population, p) # Sélection
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
            meilleure_sequence = population[0].seq
    meilleures_solutions_pairing.append(C)
f.write(str(statistics.mean(meilleures_solutions_pairing))+'\n')

for j in range(len(meilleures_solutions_random)):
    f.write(str(meilleures_solutions_pairing[j])+' ')
f.write('\n')
f.write('Mixed Pairing: ')
meilleures_solutions_mixed_pairing = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    meilleure_sequence = population[0].seq

    while (time.time()-temps_initial < temps_max): 
        appariement.mixed_pairing(population) # Appariement aléatoire
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population(population, p) # Sélection
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
            meilleure_sequence = population[0].seq
    meilleures_solutions_mixed_pairing.append(C)
f.write(str(statistics.mean(meilleures_solutions_mixed_pairing))+'\n')

for j in range(len(meilleures_solutions_random)):
    f.write(str(meilleures_solutions_mixed_pairing[j])+' ')

f.close()
