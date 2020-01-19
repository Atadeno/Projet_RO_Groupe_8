"""
Algorithme Génétique
- Croisement
"""

import ordonnancement as ord
import job

# prend deux listes d'entiers entrée
# croise ces deux listes de jobs
# retourne les deux listes d'entiers croisées


def half_crossover(L, M):
    L1 = L[0: int(len(L) / 3)]
    L2 = L[int(len(L) / 3): len(L)]

    M1 = M[0: int(len(M) / 3)]
    M2 = M[int(len(M) / 3): len(M)]

    new_L = L1 + M2
    new_M = M1 + L2
    return new_L, new_M, [[0, int(len(L) / 3)-1]]


def two_point_crossover(L, M):
    L1 = L[0: int(len(L) / 3)]
    L2 = L[int(len(L) / 3): int(2 * len(L) / 3)]
    L3 = L[int(2 * len(L) / 3): len(L)]

    M1 = M[0: int(len(M) / 3)]
    M2 = M[int(len(M) / 3): int(2 * len(M) / 3)]
    M3 = M[int(2 * len(M) / 3): len(M)]

    new_L = L1 + M2 + L3
    new_M = M1 + L2 + M3

    return new_L, new_M, [[0, int(len(L)/3)-1],[int(2*len(M)/3), len(M)-1]]


def single_point_crossover(L, M):
    L1 = L[0: int(len(L) / 3)]
    L2 = L[int(len(L) / 3): int(2 * len(L) / 3)]
    L3 = L[int(2 * len(L) / 3): len(L)]

    M1 = M[0: int(len(M) / 3)]
    M2 = M[int(len(M) / 3): int(2 * len(M) / 3)]
    M3 = M[int(2 * len(M) / 3): len(M)]

    new_M = M1 + M2 + L3
    new_L = L1 + L2 + M3

    return new_L, new_M, [[0, int(len(M)/3)-1],[int(len(M)/3), int(2*len(M)/3)-1]]


# prend deux listes d'entiers entrée
# croise ces deux listes d'entiers
# retourne les deux listes d'entiers croisées

def croiser_liste(L, M):
    try:
        len(M) != len(L)
    except:
        print("ERREUR: les longueurs des solutions à croiser ne sont pas égales")

    new_L, new_M, index_cross_domain = single_point_crossover(L, M)
    return new_L, new_M, index_cross_domain


# répare les deux listes de jobs qui ont été croisées, l'entrée c'est le résultat de la méthode dessus
# les valeurs des deux listes doivent être exactement dans l'ensemble {1,2,3 ... Nb_job}, jobs compté de 1
# une modification de réparation ne peut se faire que dans la sous-liste éxogène de numéros
def repair_lists(list_jobs_L, list_jobs_M, index_cross_domain) :
    Nb_job = len(list_jobs_L)
    index_L = []
    index_M = []
    # on remplace les jobs par leurs numéros respectifs pour les deux listes de jobs
    for job in list_jobs_L :
        index_L.append(job.numero())
    for job in list_jobs_M :
        index_M.append(job.numero())
    # visualiser les listes d'entiers
    """
    print("index_L",index_L)
    print("index_M", index_M)
    """
    # problème du comptage des jobs à partir de 1 ou de 0 résolu par cette condition
    if 0 in index_L or 0 in index_M :
        maximum = Nb_job-1
        minimum = 0
    else :
        maximum = Nb_job
        minimum = 1

    # Etape 2 : Manquants et doubles
    # on utilise la méthode set de la classe set pour détecter les entiers manquant respectivement dans index_L et index_M
    missing_L = list(set(index_M).difference(index_L)) # ce sont aussi les doubles de index_M
    missing_M = list(set(index_L).difference(index_M)) # ce sont aussi les doubles de index_L
    """
    print("missing_L",missing_L)
    print("missing_M", missing_M)
    """
    # Etape 3 : Remplacement
    # on applique la stratégie de remplacement, ... est optimale
    #replace_no_domain_restriction(index_L,index_M, missing_L, missing_M)
    #replace_domain_restriction_progress(index_L, index_M, missing_L, missing_M, index_cross_domain)
    replace_domain_restriction_inverted(index_L, index_M, missing_L, missing_M, index_cross_domain)
    """
    print("index_L after replace",index_L)
    print("index_M after replace", index_M)
    """
    # On revient aux jobs
    well_formed_kids_L = [None for i in range(0, Nb_job)]
    well_formed_kids_M = [None for i in range(0, Nb_job)]

    for job in list_jobs_L + list_jobs_M:  # prob job potentiel manquant dans les deux listes
        for i in range(0, Nb_job):
            if job.numero() == index_L[i]:
                well_formed_kids_L[i] = job
            if job.numero() == index_M[i]:
                well_formed_kids_M[i] = job

        # afficher le réparage des jobs
    """
    print("well_formed_kids_L")
    for job in well_formed_kids_L:
        print(job.numero(), "  ", end = '')
        # job.afficher()
    print(" ")
    print("well_formed_kids_M")
    for job in well_formed_kids_M:
        print(job.numero(), "  ", end = '')
        # job.afficher()
    """
    return well_formed_kids_L, well_formed_kids_M


# remplacement sans contrainte sur le domaine de réparation dans les deux listes
def replace_no_domain_restriction(index_L,index_M,missing_L, missing_M) :

    for i in range(0,len(missing_L)) :
        # remplacements dans index_L
        index = index_L.index(missing_M[i])
        index_L.remove(missing_M[i])
        index_L.insert(index, missing_L[i])

        # remplacements dans index_M
        index = index_M.index(missing_L[i])
        index_M.remove(missing_L[i])
        index_M.insert(index, missing_M[i])


# remplacement avec chagement que dans les parties fixes des listes, le parcours des parties fixes dans les listes se fait du début vers la fine des deux listes
def replace_domain_restriction_progress(index_L, index_M, missing_L, missing_M, index_cross_domain) :
    """
    print("domain" , index_cross_domain)
    """

    for i in range(0,len(missing_L)) :
        # remplacement dans le(s) domaine(s) fixe(s) de index_L
        for j in range(len(index_cross_domain)) :
            bool_L = missing_M[i] in index_L[index_cross_domain[j][0]:index_cross_domain[j][1]+1]
            """
            print("bool_L iter ",j," ",bool_L)
            """
            if bool_L == True :
                # remplacements dans index_L[index_cross_domain[j][0]:index_cross_domain[j][1]+1]
                for k in range(index_cross_domain[j][0],index_cross_domain[j][1]+1) :
                    if index_L[k]==missing_M[i] :
                        index_L[k] = missing_L[i]
                break

        # remplacement dans le(s) domaine(s) fixe(s) de index_M
        for j in range(len(index_cross_domain)) :
            bool_M = missing_L[i] in index_M[index_cross_domain[j][0]:index_cross_domain[j][1]+1]
            """
            print("bool_M iter ", j, " ", bool_M)
            """
            if bool_M == True :
                # remplacements dans index_M[index_cross_domain[j][0]:index_cross_domain[j][1]+1]
                for k in range(index_cross_domain[j][0],index_cross_domain[j][1]+1) :
                    if index_M[k]==missing_L[i] :
                        index_M[k] = missing_M[i]
                break

# remplacement avec chagement que dans les parties fixes des listes, le parcours des parties fixes dans les listes de manière inversé : index_L du début vers la fin,
# et index_M de sa fin vers son début
def replace_domain_restriction_inverted(index_L, index_M, missing_L, missing_M, index_cross_domain) :

    for i in range(0, len(missing_L)):
        # remplacement dans le(s) domaine(s) fixe(s) de index_L
        for j in range(len(index_cross_domain)):
            bool_L = missing_M[i] in index_L[index_cross_domain[j][0] : index_cross_domain[j][1]+1]
            """
            print("bool_L iter ", j, " ", bool_L)
            """
            if bool_L == True:
                # remplacements dans index_L
                for k in range(index_cross_domain[j][0],index_cross_domain[j][1]+1) :
                    if index_L[k]==missing_M[i] :
                        index_L[k] = missing_L[i]
                break

        # remplacement dans le(s) domaine(s) fixe(s) de index_M
        for j in range(len(index_cross_domain) - 1, -1, -1):
            bool_M = missing_L[i] in index_M[index_cross_domain[j][0] : index_cross_domain[j][1]+1]
            """
            print("bool_M iter ", j, " ", bool_M)
            """
            if bool_M == True:
                # remplacements dans index_M
                for k in range(index_cross_domain[j][0],index_cross_domain[j][1]+1) :
                    if index_M[k]==missing_L[i] :
                        index_M[k] = missing_M[i]
                break


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

    return kid1, kid2


# prend une liste de population de taille N
# réalise le croisement deux à deux
# retourne une nouvelle population de taille 2*N
def generate(population):
    kids = []
    for index in range(int(len(population)/2)):
        kid1, kid2 = create_two_kids(population[2*index], population[2*index + 1])
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

    # listes de 5 job pour test l'indexation R et W :
    listeL = [job1, job4, job5, job3, job2]
    listeM = [job5, job3, job4, job1, job2]

    liste1 = [job1, job4, job5, job3, job2, job6]
    liste2 = [job5, job3, job4, job6, job1, job2]


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

    """
    population = [parent_1, parent_2, parent_3, parent_4, parent_5, parent_6]
    new_population = generate(population)
    print(len(new_population))
    for individu in population:
        individu.afficher()
    
    # R : Test de la fonction repair pour deux listes des jobs  :
    #index_L,index_M = croiser_liste(L,M)  #le croisement super
    """

    # Tests de réparage
    #L_index, M_index = croiser_liste(listeL, listeM)
    #repair1(L_index, M_index)
    #repair2(L_index, M_index)

    L_index, M_index, index_cross_domain = croiser_liste(listeL, listeM)

    repair_lists(L_index, M_index, index_cross_domain)


