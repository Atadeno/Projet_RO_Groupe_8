import generation
import appariement
import croisement
import mutation
import selection
import ordonnancement
import time
import statistics

### Algorithme Génétique ###

N = 10
p = 0.8
T = 10

fichier = "tai21.txt"

f = open("test_mutation_2.txt", "w")
f.write('Test Differentes Valeurs de Mutation' +'\n')
temps_max = 360 # Temps maximal d'un calcul en secondes

mutations = [7,8,9,10,11,12,13]

population_initiale = generation.generation_aleatoire(fichier, N) # Génération
population_initiale = sorted(population_initiale, key=lambda ordonnancement: ordonnancement.dur)

Cmin = population_initiale[0].dur # Meilleur résultat départ
Cmax = population_initiale[-1].dur # Pire résultat départ

solutions_initiales = [population_initiale[i].dur for i in range(len(population_initiale))]
Moy = statistics.mean(solutions_initiales)

f.write('Cmin: '+str(Cmin)+' '+'Cmax: '+str(Cmax)+' '+'Moyenne: '+str(Moy)+'\n')

for r in range(len(mutations)):
    f.write(str(mutations[r])+'%'+'\n')
    meilleures_solutions = []
    for i in range(10): # On fait 10 epoch
        temps_initial = time.time()
        C = Cmin
        population = population_initiale
        #e = 0
        while (time.time()-temps_initial < temps_max):
            appariement.C_pairing(population)
            population = croisement.croisement_population(population) # Croisement
            mutation.mutation_population(population, mutations[r]) # Mutation
            population = selection.selection_population_tournoi(population, T) # Sélection 80% meilleurs
            #e+=1
            if C > population[0].dur: # Sauvegarde du meilleur individu
                C = population[0].dur
        meilleures_solutions.append(C)
    f.write(str(statistics.mean(meilleures_solutions))+'\n')

    for j in range(len(meilleures_solutions)):
        f.write(str(meilleures_solutions[j])+' ')
    f.write('\n')
    #f.write('Nombre de generation: '+str(e)+'\n')
f.close()
