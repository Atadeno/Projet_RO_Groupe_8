import generation
import appariement
import croisement
import mutation
import selection
import ordonnancement

### Algorithme Génétique ###

N = 1000
p = 0.8

fichier = "jeu2.txt"

population = generation.generation_aleatoire(fichier, N) # Génération
population = sorted(population, key=lambda ordonnancement: ordonnancement.dur)
Cmin = population[0].dur # Meilleur résultat
meilleure_sequence = population[0].seq # Meilleure séquence
t = 0

while (t < 1000):
    appariement.appariement_population(population) # Appariement aléatoire
    population = croisement.croisement_population(population) # Croisement
    mutation.mutation_population(population) # Mutation
    population = selection.selection_population(population, p) # Sélection
    if Cmin > population[0].dur: # Sauvegarde du meilleur individu
        print("Nouvel Alpha trouvé")
        Cmin = population[0].dur
        meilleure_sequence = population[0].seq
    t-=-1
    print(t)

ordo = ordonnancement.Ordonnancement(population[0].nb_machines) # Création d'un nouvel ordonnancement
ordo.ordonnancer_liste_job(meilleure_sequence)
ordo.afficher() # Affichage de notre solution