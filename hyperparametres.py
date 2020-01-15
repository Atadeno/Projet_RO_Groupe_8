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
T = 10

fichier = "tai21.txt"

f = open("test_selection.txt", "w")
f.write('Test Differentes Selections' +'\n')
temps_max = 3 # Temps maximal d'un calcul en secondes

population_initiale = generation.generation_aleatoire(fichier, N) # Génération
population_initiale = sorted(population_initiale, key=lambda ordonnancement: ordonnancement.dur)

Cmin = population_initiale[0].dur # Meilleur résultat départ
Cmax = population_initiale[-1].dur # Pire résultat départ

solutions_initiales = [population_initiale[i].dur for i in range(len(population_initiale))]
Moy = statistics.mean(solutions_initiales)

f.write('Cmin: '+str(Cmin)+' '+'Cmax: '+str(Cmax)+' '+'Moyenne: '+str(Moy)+'\n')

f.write('P Meilleurs: ')
meilleures_solutions_p_meilleurs = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    e = 0
    while (time.time()-temps_initial < temps_max): 
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population_p_meilleurs(population, p) # Sélection 80% meilleurs
        e+=1
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
    meilleures_solutions_p_meilleurs.append(C)
f.write(str(statistics.mean(meilleures_solutions_p_meilleurs))+'\n')

for j in range(len(meilleures_solutions_p_meilleurs)):
    f.write(str(meilleures_solutions_p_meilleurs[j])+' ')
f.write('\n')
f.write('Nombre de generation: '+str(e)+'\n')

f.write('Roulette: ')
meilleures_solutions_roulette = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    e = 0
    while (time.time()-temps_initial < temps_max): 
        appariement.C_pairing(population)
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population_roulette(population) # Sélection par tounois de T individus
        e+=1
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
    meilleures_solutions_roulette.append(C)
f.write(str(statistics.mean(meilleures_solutions_roulette))+'\n')

for j in range(len(meilleures_solutions_roulette)):
    f.write(str(meilleures_solutions_roulette[j])+' ')
f.write('\n')
f.write('Nombre de generation: '+str(e)+'\n')

f.write('Tournois: ')
meilleures_solutions_tournois = []

for i in range(10): # On fait 10 epoch
    temps_initial = time.time()
    C = Cmin
    population = population_initiale
    e = 0
    while (time.time()-temps_initial < temps_max): 
        appariement.C_pairing(population)
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population_tournoi(population,T) # Sélection par tounois de T participants
        e+=1
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
    meilleures_solutions_tournois.append(C)
f.write(str(statistics.mean(meilleures_solutions_tournois))+'\n')

for j in range(len(meilleures_solutions_tournois)):
    f.write(str(meilleures_solutions_tournois[j])+' ')
f.write('\n')
f.write('Nombre de generation: '+str(e)+'\n')
f.close()
