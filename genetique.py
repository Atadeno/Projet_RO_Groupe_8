import generation
import appariement
import croisement
import mutation
import selection
import ordonnancement
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np

### Algorithme Génétique ###

N = 5000
p = 0.5
T = 2

fichiers = ["tai21.txt"]#["tai01.txt", "tai02.txt", "tai11.txt", "tai12.txt", "tai21.txt", "tai22.txt", "tai31.txt", "tai32.txt", "tai41.txt", "tai42.txt", "tai51.txt", "tai52.txt"]
optimum = [2297]#[1278, 1359, 1582, 1659, 2297, 2099, 2724, 2834, 2991, 2867, 3874, 3704]

f = open("resultats_opti.txt", "w")
f.write('Fichiers  | Best | DRel | Moyenne | Depart- | Depart+ |' +'\n')
temps_max = 60 # Temps maximal d'un calcul en secondes (ici 10 minutes)
Cmin_tab=[]
Cmax_tab=[]
Moy_tab=[]
temps_x=1

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
    now1=time.time()
    while (C > optimal) and (time.time()-temps_initial < temps_max): 
        if time.time()-now1 >= temps_x:
            population = sorted(population, key = lambda ordonnancement: ordonnancement.dur)
            Cmin_tab.append(population[0].dur)
            Cmax_tab.append(population[-1].dur)
            solutions = [population[i].dur for i in range(len(population))]
            Moy_tab.append(statistics.mean(solutions))
            now1=time.time()
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 10) # Mutation
        population = selection.selection_population_p_meilleurs(population,p) # Sélection par tounois
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

liste_temps= np.linspace(0, temps_x*len(Cmax_tab), num=len(Cmax_tab))
print(liste_temps)
plt.plot(np.array(Cmin_tab),color='g')
plt.plot(np.array(Cmax_tab),color='r')
plt.plot(np.array(Moy_tab),color='k')
plt.show()