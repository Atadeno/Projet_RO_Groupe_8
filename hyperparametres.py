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

fichiers = ["tai21.txt"]

m = input("Entrez le nom du fichier: test_appariement_")
f = open("test_appariement_"+ m +".txt", "w")
f.write('Test Différents Appariements' +'\n')
temps_max = 360 # Temps maximal d'un calcul en secondes (ici 10 minutes)

population_initiale = generation.generation_aleatoire(fichiers[i], N) # Génération
population_initiale = sorted(population, key=lambda ordonnancement: ordonnancement.dur)

Cmin = population_initiale[0].dur # Meilleur résultat départ
C = Cmin
Cmax = population[-1]_initiale.dur # Pire résultat départ

solutions_initiales = [population[i].dur for i in range(len(population))]
Moy = statistics.mean(solutions_initiales)

meilleure_sequence = population[0].seq # Meilleure séquence
temps_initial = time.time()

    while (time.time()-temps_initial < temps_max): 
        appariement.appariement_population(population) # Appariement aléatoire
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population(population, p) # Sélection
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
