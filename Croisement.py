"""
Algorithme Génétique
- sCroisement
"""

import ordonnancement
import job


def swap(A,B,i,j):
    TEMP_B = B[j]
    B[j] = A[i]
    A[i] = TEMP_B
    return A,B

# prend deux liste d'entiers entrée
# coise ces deux listes d'entiers
# retourne les deux listes d'entiers croisées
def croiser_liste(L,M):
    try:
        len(M) != len(L)
    except:
        print("ERREUR: les longueurs des solutions à croiser ne sont pas égales")
    L1 = L[0: int(len(L)/3)]
    L2 = L[int(len(L)/3): int(2*len(L)/3)]
    L3 = L[int(2*len(L)/3): len(L)]

    M1 = M[0: int(len(M) / 3)]
    M2 = M[int(len(M) / 3): int(2 * len(M) / 3)]
    M3 = M[int(2 * len(M) / 3): len(M)]

    new_L = L1+M2+L3
    new_M = M1+L2+M3

    index_L = [job.num for job in new_L]
    index_M = [job.num for job in new_M]

    index_L = new_L
    index_M = new_M




    for index in new_L:
        if index_L.count(index)>1:
            print()
    print()
    for index in new_M:
        if index_M.count(index) > 1:
            print(index)
    print("indexes_L", index_L)
    print("indexes_M", index_M)


    return index_L, index_M

# prend deux parents
# retourne deux enfants croisés
def create_two_kids(parent_1, parent_2):
    liste_jobs_parent_1 = parent_1.sequence()
    liste_jobs_parent_2 = parent_2.sequence()

    l1 , l2 = croiser_liste(liste_jobs_parent_1, liste_jobs_parent_2)

    kid1 = ordonnancement.Ordonnancement(10)
    kid2 = ordonnancement.Ordonnancement(10)

    kid1.ordonnancer_liste_job(l1)
    kid2.ordonnancer_liste_job(l2)
    print()


    return kid1, kid2

# prend une liste de population de taille N
# réalise le croisement deux à deux
# retourne une nouvelle population de taille 2*N
def generate(population):
    kids = []
    for index in range(int(len(population)/2)):
        kid1, kid2 = create_two_kids(population[index],population[index+1])
        kids.append(kid1)
        kids.append(kid2)
    return population + kids

if __name__ == '__main__':
    number_of_jobs = 10
    job1 = job.Job(1, [46,61,3,51,37,79,83,22,27,24])
    job2 = job.Job(2, [52,87,1,24,16,93,87,29,92,47])
    job3 = job.Job(3, [79,51,58,21,42,68,38,99,75,39])
    job4 = job.Job(4, [45,25,85,57,47,75,38,25,94,66])
    job5 = job.Job(5, [97,73,33,69,94,37,86,98,18,41])
    job6 = job.Job(6, [10,93,71,51,14,44,67,55,41,46])
    
    liste1 = [job1, job4, job5, job3, job2, job6]
    liste2 = [job5, job3, job4, job6, job1, job2]
    liste3 = [job1, job2, job3, job4, job5, job6]
    liste4 = [job6, job5, job4, job3, job2, job1]
    liste5 = [job6, job4, job5, job3, job1, job2]
    liste6 = [job1, job6, job2, job5, job3, job4]
    
    parent_1 = ordonnancement.Ordonnancement(10)
    parent_2 = ordonnancement.Ordonnancement(10)
    parent_3 = ordonnancement.Ordonnancement(10)
    parent_4 = ordonnancement.Ordonnancement(10)
    parent_5 = ordonnancement.Ordonnancement(10)
    parent_6 = ordonnancement.Ordonnancement(10)
    
    parent_1.ordonnancer_liste_job(liste1)
    parent_2.ordonnancer_liste_job(liste2)
    parent_3.ordonnancer_liste_job(liste3)
    parent_4.ordonnancer_liste_job(liste4)
    parent_5.ordonnancer_liste_job(liste5)
    parent_6.ordonnancer_liste_job(liste6)
    
    population = [parent_1,parent_2, parent_3, parent_4, parent_5, parent_6]

    new_population = generate(population)
    for person in new_population:
        print("person ",person)






