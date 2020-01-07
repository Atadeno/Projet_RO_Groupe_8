import generation
import appariement
import croisement
import mutation
import selection
import ordonnancement
import time

### Algorithme Génétique ###

N = 1000
p = 0.8

fichiers = ["jeu1.txt", "jeu2.txt", "tai01.txt", "tai02.txt", "tai11.txt", "tai12.txt", "tai21.txt", "tai22.txt", "tai31.txt", "tai32.txt", "tai41.txt", "tai42.txt", "tai51.txt", "tai52.txt"]
optimum = [54, 704, 1278, 1359, 1582, 1659, 2297, 2099, 2724, 2834, 2991, 2867, 3874, 3704]

f = open("resultats.txt", "w")
f.write('Fichier | Cmin | Optimal | Ecart' +'\n')
temps_max = 1 # Temps maximal d'un calcul en secondes (ici 10 minutes)

for i in range(len(fichiers)):

    print("Fichier:",fichiers[i])
    print("\n")

    population = generation.generation_aleatoire(fichiers[i], N) # Génération
    population = sorted(population, key=lambda ordonnancement: ordonnancement.dur)

    Cmin = population[0].dur # Meilleur résultat
    meilleure_sequence = population[0].seq # Meilleure séquence
    temps_initial = time.time()
    optimal = optimum[i] # Optimal connu pour arrêt

    while (Cmin > optimal) and (time.time()-temps_initial < temps_max): 
        appariement.appariement_population(population) # Appariement aléatoire
        population = croisement.croisement_population(population) # Croisement
        mutation.mutation_population(population, 20) # Mutation 20%
        population = selection.selection_population(population, p) # Sélection
        if Cmin > population[0].dur: # Sauvegarde du meilleur individu
            Cmin = population[0].dur
            meilleure_sequence = population[0].seq

    ordo = ordonnancement.Ordonnancement(population[0].nb_machines) # Création d'un nouvel ordonnancement
    ordo.ordonnancer_liste_job(meilleure_sequence)
    ordo.afficher() # Affichage de notre solution
    print("\n")
    f.write(fichiers[i]+' '+str(Cmin)+' '+str(optimal)+' '+str(round(100*(Cmin-optimal)/optimal,1))+'%'+'\n')
f.close()