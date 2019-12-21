"""
Algorithme Génétique
- sCroisement

"""

import ordonnancement as ord
import job


def swap(A, B, i, j):
    TEMP_B = B[j]
    B[j] = A[i]
    A[i] = TEMP_B
    return A, B


# prend deux liste d'entiers entrée
# croise ces deux listes d'entiers
# retourne les deux listes d'entiers croisées
def croiser_liste(L, M):
    try:
        len(M) != len(L)
    except:
        print("ERREUR: les longueurs des solutions à croiser ne sont pas égales")
    L1 = L[0: int(len(L) / 3)]
    L2 = L[int(len(L) / 3): int(2 * len(L) / 3)]
    L3 = L[int(2 * len(L) / 3): len(L)]

    M1 = M[0: int(len(M) / 3)]
    M2 = M[int(len(M) / 3): int(2 * len(M) / 3)]
    M3 = M[int(2 * len(M) / 3): len(M)]

    new_L = L1 + M2 + L3
    new_M = M1 + L2 + M3
    # R : y avait job.num alors que job est un int
    index_L = [job for job in new_L]
    index_M = [job for job in new_M]

    index_L = new_L
    index_M = new_M
    # R : j'ai commenté ceci, l'utilité détecter les doublons me parait
    """"
    for index in new_L:
        if index_L.count(index) > 1:
            print()
    print()
    for index in new_M:
        if index_M.count(index) > 1:
            print(index)
    
    print("indexes_L", index_L)
    print("indexes_M", index_M)
    """""
    return index_L, index_M

# R : répare les deux listes de jobs qui ont été croisées, l'entrée c'est le résulter de la méthode dessus h
# les valeurs des deux liste doivent etre exactement dans l'ensemble {1,2,3 ... Nb_job}, jobs compté de 1
# une modification de réparation ne peut se faire que dans la sous-liste éxogène de numéros
def repair(list_jobs_L, list_jobs_M) :
    Nb_job = len(list_jobs_L)
    index_L= []
    index_M = []
    # On remplace les jobs par leurs numeros respctifs pour les deux listes de jobs
    for job in list_jobs_L :
        index_L.append(job.numero())
    for job in list_jobs_M :
        index_M.append(job.numero())
    # visualiser les listes d'entiers
    """""
    print("index_L",index_L)
    print("index_M", index_M)
    """""
    # problème du comptage des jobs à partir de 1 ou de 0 résolu par cette condition
    if 0 in index_L or 0 in index_M :
        maximum = Nb_job-1
        minimum = 0
    else :
        maximum = Nb_job
        minimum = 1

    # Etape 1 : Doublons
    # ces deux listes contiendront des tuples des élèments doublés (dans la sous-liste exogène) avec leurs positions respectives, les positions  doivent etre
    # l'intervalle [Nb_job//3,2*Nb_job//3]
    doubled_elements_L = []
    doubled_elements_M = []
    for i in range(Nb_job//3,2*Nb_job//3) : # l'intervalle est bien respecté selon la règle dans la fonction de croisement
        if index_L.count(index_L[i]) > 1 :
            doubled_elements_L.append((index_L[i],i))
        if index_M.count(index_M[i]) > 1 :
            doubled_elements_M.append((index_M[i],i))
    # tester la détection des doublons
    """""
    print("Doubles L",doubled_elements_L)
    print("Doubles M", doubled_elements_M)
    """""
    # Etape 2 : Manquants
    #ces deux listes contiendront des tuples des élèments manquants
    missing_elements_L = []
    missing_elements_M = []
    for i in range(minimum, maximum+1):
        indice_L = False
        indice_M = False
        for j in range(0, Nb_job):
            if i==index_L[j]:
                indice_L = True
            if i==index_M[j]:
                indice_M = True
        if indice_L == False:
            missing_elements_L.append(i)
        if indice_M == False:
            missing_elements_M.append(i)
    # tester la détection des manquants
    """""
    print("Missing L", missing_elements_L)
    print("Missing M", missing_elements_M)
    """""
    #Etape 3 : Remplacer les doublons par les manquants
    # on remplace les doublons dans les listes exogènes par les manquants
    for i in range(0, len(doubled_elements_L)):
        index_L[doubled_elements_L[i][1]] = missing_elements_L[i]
        index_M[doubled_elements_M[i][1]] = missing_elements_M[i]
    # Retourne les listes des entiers après croisement
    # print pour tests
    """""
    print(index_L)
    print(index_M)
    """""
    # On revient aux jobs
    well_formed_kids_L = [ None for i in range(0,Nb_job)]
    well_formed_kids_M = [ None for i in range(0,Nb_job)]

    for job in list_jobs_L+list_jobs_M : # prob job potentiel manquant dans les deux listes
        for i in range(0,Nb_job) :
            if job.numero() == index_L[i] :
                well_formed_kids_L[i] = job
            if job.numero() == index_M[i] :
                well_formed_kids_M[i] = job

    # afficher le réparage des jobs
    """""
    print("well_formed_kids_L")
    for job in well_formed_kids_L :
        job.afficher()
    print("well_formed_kids_M")
    for job in well_formed_kids_M :
        job.afficher()
    """""
    return well_formed_kids_L , well_formed_kids_M




# prend deux parents
# retourne deux enfants croisés
def create_two_kids(parent_1, parent_2):
    liste_jobs_parent_1 = parent_1.sequence()
    liste_jobs_parent_2 = parent_2.sequence()

    l1, l2 = croiser_liste(liste_jobs_parent_1, liste_jobs_parent_2)

    # R : réparage
    l1, l2 = repair(l1,l2)

    kid1 = ord.Ordonnancement(10)
    kid2 = ord.Ordonnancement(10)

    kid1.ordonnancer_liste_job(l1)
    kid2.ordonnancer_liste_job(l2)
    print()

    return kid1, kid2


# prend une liste de population de taille N
# réalise le croisement deux à deux
# retourne une nouvelle population de taille 2*N
def generate(population):
    kids = []
    for index in range(int(len(population) / 2)):
        kid1, kid2 = create_two_kids(population[index], population[index + 1])
        kids.append(kid1)
        kids.append(kid2)
    return population + kids


if __name__ == '__main__':
    # R : génération des enfants commentée


    number_of_machines = 10

    job1 = job.Job(1, [46, 61, 3, 51, 37, 79, 83, 22, 27, 24])
    job2 = job.Job(2, [52, 87, 1, 24, 16, 93, 87, 29, 92, 47])
    job3 = job.Job(3, [79, 51, 58, 21, 42, 68, 38, 99, 75, 39])
    job4 = job.Job(4, [45, 25, 85, 57, 47, 75, 38, 25, 94, 66])
    job5 = job.Job(5, [97, 73, 33, 69, 94, 37, 86, 98, 18, 41])
    job6 = job.Job(6, [10, 93, 71, 51, 14, 44, 67, 55, 41, 46])

    liste1 = [job1, job4, job5, job3, job2, job6]
    liste2 = [job5, job3, job4, job6, job1, job2]

    """""
    liste3 = [job1, job2, job3, job4, job5, job6]
    liste4 = [job6, job5, job4, job3, job2, job1]
    liste5 = [job6, job4, job5, job3, job1, job2]
    liste6 = [job1, job6, job2, job5, job3, job4]

    parent_1 = ord.Ordonnancement(10)
    parent_2 = ord.Ordonnancement(10)
    parent_3 = ord.Ordonnancement(10)
    parent_4 = ord.Ordonnancement(10)
    parent_5 = ord.Ordonnancement(10)
    parent_6 = ord.Ordonnancement(10)

    parent_1.ordonnancer_liste_job(liste1)
    parent_2.ordonnancer_liste_job(liste2)
    parent_3.ordonnancer_liste_job(liste3)
    parent_4.ordonnancer_liste_job(liste4)
    parent_5.ordonnancer_liste_job(liste5)
    parent_6.ordonnancer_liste_job(liste6)

    population = [parent_1, parent_2, parent_3, parent_4, parent_5, parent_6]
    new_population = generate(population)
    for person in new_population:
    print("person ", person)
    """""

    # R : Test de la fonction repair pour deux listes des jobs  :
    #index_L,index_M = croiser_liste(L,M)  #le croisement super
    repair(croiser_liste(liste1,liste2)[0],croiser_liste(liste1,liste2)[1])


