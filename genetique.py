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

fichiers = ["tai01.txt", "tai02.txt", "tai11.txt", "tai12.txt", "tai21.txt", "tai22.txt", "tai31.txt", "tai32.txt", "tai41.txt", "tai42.txt", "tai51.txt", "tai52.txt"]
optimum = [1278, 1359, 1582, 1659, 2297, 2099, 2724, 2834, 2991, 2867, 3874, 3704]

f = open("resultats_opti.txt", "w")
f.write('Fichiers  | Best | DRel | Moyenne | Depart- | Depart+ |' +'\n')
temps_max = 600   # Temps maximal d'un calcul en secondes (ici 10 minutes)

for i in range(len(fichiers)):

    print("Fichier:",fichiers[i])
    
    population = generation.generation_aleatoire(fichiers[i], N) # Génération
    population = sorted(population, key=lambda ordonnancement: ordonnancement.dur)

    Cmin = population[0].dur # Meilleur résultat départ
    C = Cmin
    Cmax = population[-1].dur # Pire résultat départ

    solutions_initiales = [population[i].dur for i in range(len(population))]
    Moy = statistics.mean(solutions_initiales)

    meilleure_sequence = population[0].seq # Meilleure séquence
    temps_initial = time.time()
    optimal = optimum[i] # Optimal connu pour arrêt

    while (C > optimal) and (time.time()-temps_initial < temps_max): 
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population_tournoi(population, T) # Sélection par tounois
        appariement.C_pairing(population)
        if C > population[0].dur: # Sauvegarde du meilleur individu
            C = population[0].dur
            meilleure_sequence = population[0].seq

    ordo = ordonnancement.Ordonnancement(population[0].nb_machines) # Création d'un nouvel ordonnancement
    ordo.ordonnancer_liste_job(meilleure_sequence)
    """
    ordo.afficher() # Affichage de notre solution
    print("\n")
    """
    print("Done")
    f.write(fichiers[i]+'   '+str(C)+'   '+str(round(100*(Cmin-C)/C,1))+'%'+'   '+str(round(Moy,1))+'     '+str(Cmin)+'      '+str(Cmax)+'\n')
f.close()