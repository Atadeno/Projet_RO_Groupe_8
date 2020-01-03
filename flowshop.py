#!/usr/bin/env python

"""Résolution du flowshop de permutation : 

 - par algorithme NEH
 - par une méthode évaluation-séparation
 """
import copy
from datetime import datetime

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019'

import job
import ordonnancement
import sommet
import itertools

import heapq

MAXINT = 10000


class Flowshop():
    def __init__(self, nb_jobs=0, nb_machines=0, l_job=[]):
        self.nb_jobs = nb_jobs
        self.nb_machines = nb_machines
        self.l_job = l_job

    def get_job_by_id(self, job_id=0):
        for job in self.l_job:
            if job.num == job_id:
                return job

    def nombre_jobs(self):
        return self.nb_jobs

    def nombre_machines(self):
        return self.nb_machines

    def liste_jobs(self, num):
        return self.l_job[num]

    def trier_jobs(self):
        L = [()] * (len(self.l_job))
        for index in range(len(self.l_job)):
            L[index] = tuple([self.l_job[index], self.l_job[index].duree()])
        L.sort(key=lambda tup: tup[1], reverse=True)
        index = 0;
        for tup in L:
            self.l_job[index] = tup[0]
            index += 1

    def definir_par(self, nom):
        """ crée un problème de flowshop à partir d'un fichier """
        # ouverture du fichier en mode lecture
        fdonnees = open(nom, "r")
        # lecture de la première ligne
        ligne = fdonnees.readline()
        l = ligne.split()  # on récupère les valeurs dans une liste
        self.nb_jobs = int(l[0])
        self.nb_machines = int(l[1])
        ordo = ordonnancement.Ordonnancement(self.nb_machines)
        for i in range(self.nb_jobs):
            ligne = fdonnees.readline()
            l = ligne.split()
            # on transforme les chaînes de caractères en entiers
            l = [int(i) for i in l]
            j = job.Job(i, l)
            ordo.ordonnancer_job(j)
            self.l_job += [j]
        # fermeture du fichier
        fdonnees.close()
        return ordo

    # exo 4 A REMPLIR
    def min_ordo(self, L):
        m = MAXINT
        for ordo in L:
            if ordo.duree()<m:
                temp_ordo = ordo
                m = ordo.duree
        return temp_ordo
    # renvoie une liste selon lordre NEH

    def permutations_with_order(self, L):
        M = [()]
        for i in range(len(L)):
            temp = L[0:len(L) - 1]
            temp.insert(i,L[-1])
            M.append(tuple(temp))

        M.remove(M[0])
        return M



    def creer_liste_NEH(self):
        m = MAXINT
        # liste_NEH est le réslutat de l'algorithme NEH
        liste_NEH = ordonnancement.Ordonnancement(self.nb_machines)
        # etape 1: Trier les jobs par ordre croissant de leur durée totale
        self.trier_jobs()
        # ajout du job ayant la durée totale minimale à une liste l
        # l contient des numéros de job
        l = [self.l_job[0].num]
        for index in range(1,self.nb_jobs):
            # ajout du job suivant
            l.append(self.l_job[index].numero())
            # list_permutation contient des tuples
            # chaque tuple est une permutation
            # des elements de la liste l
            # list_permutation contient toutes
            # les permutation
            #list_permutation = list(itertools.permutations(l))

            list_permutation = self.permutations_with_order(l)
            #print(list_permutation)
            # list_ordo est une liste qui va contenir tous
            # les ordonnancements générés par liste_permutation
            list_ordo = []
            for tup in list_permutation:
                # list_job contient une liste de jobs crées
                # par les indices contenus dans chaque element
                # de list_permutation
                list_jobs=[]
                for i in tup:
                    list_jobs.append(self.get_job_by_id(i))
                ordo = ordonnancement.Ordonnancement(self.nb_machines)
                ordo.ordonnancer_liste_job(list_jobs)
                list_ordo.append(ordo)
            m1 = MAXINT
            # on cherche dans cette boucle l'ordonnancement
            # qui est de durée minimale
            # la variable temp_ordo contient l'ordonnancement
            # de durée minimale
            for ordo in list_ordo:
                if ordo.duree()<m1:
                    #temp_ordo = copy.deepcopy(ordo)
                    temp_ordo = ordo
                    m1 = ordo.duree()
            # la fonction to_index() renvoie une liste contenant
            # les numéros des jobs d'un ordonnancement
            # la liste l mémorise les indices déja visités et enregistré
            # cela évite lors de l'énumération des différentes
            # permutations d'éviter d'énumérer des combinaisons
            # qui ne sont pas intéréssantes
            l=temp_ordo.to_index()
        liste_NEH = temp_ordo
        return liste_NEH

    # exo 5 A REMPLIR

    # calcul de r_kj tenant compte d'un ordo en cours
    def calculer_date_dispo(self, ordo, machine, new_job):
        """r = 0
        for i in range(machine):
            r=r+new_job.duree_operation(i)
        return r"""
        new_ordo = copy.copy(ordo)
        new_ordo.ordonnancer_job(new_job)
        return new_ordo.date_debut_operation(new_job, machine)




    # calcul de q_kj tenant compte d'un ordo en cours
    def calculer_duree_latence(self, ordo, machine, new_job):
        """q = 0
        for i in range(machine, self.nb_machines):
            q = q+ new_job.duree_operation(i)
        return q"""
        new_ordo = copy.copy(ordo)
        ordo.ordonnancer_job(new_job)
        fin = new_ordo.date_disponibilite(new_ordo.nb_machines-1)
        debut = new_ordo.date_disponibilite(machine)
        return fin-debut

    # calcul de la somme des durées des opérations d'une liste
    # exécutées sur une machine donnée
    def calculer_duree_jobs(self, machine, liste_jobs):
        jobs = [self.get_job_by_id(i) for i in liste_jobs]
        return sum([job.duree_operation(machine) for job in jobs])
    # calcul de la borne inférieure en tenant compte d'un ordonnancement en cours
    def calculer_borne_inf_by_machine(self, ordo, liste_jobs, machine):
        r = []
        p = 0
        q = []
        for i in liste_jobs:
            r.append(self.calculer_date_dispo(ordo, machine, self.get_job_by_id(i)))
            p += self.calculer_duree_jobs(machine, [machine])
            q.append(self.calculer_duree_latence(ordo, machine, self.get_job_by_id(i)))

        return min(r) + p + min(q)
    def calculer_borne_inf(self, ordo, list_jobs):
        L = []
        for i in range(self.nb_machines-1):
            L.append(self.calculer_borne_inf_by_machine(ordo, list_jobs, i))
        return max(L)


    # exo 6 A REMPLIR
    # procédure par évaluation et séparation
    def evaluation_separation_(self):
        #flow_shop = self.Flowshop()
        ordo = flow_shop.definir_par("jeu2.txt")
        ordo.afficher()
        liste_NEH = flow_shop.creer_liste_NEH()
        # liste = [3, 2, 0, 1]
        liste = ordo.to_index()
        val = flow_shop.calculer_borne_inf(ordo, liste)
        s = sommet.Sommet([], liste, val, 0)
        print("AAAAAAAAAAAAAAAAAAA", s)

        heap = []
        heapq.heappush(heap, s)
        opt = 1000000
        seq_opt = []

        while len(heap) != 0:
            s = heapq.heappop(heap)
            if len(s.jobs_non_places()) == 0:
                ordo = ordonnancement.Ordonnancement(flow_shop.nb_machines)
                list_jobs = [flow_shop.get_job_by_id(i) for i in s.sequence()]
                ordo.ordonnancer_liste_job(list_jobs)
                if ordo.duree() <= opt:
                    opt = ordo.duree()
                    seq_opt = s.sequence()
            else:
                for j in s.jobs_non_places():
                    print(s.jobs_non_places())
                    new_seq = copy.deepcopy(s.sequence()) + [j]
                    new_non_place = copy.deepcopy(s.jobs_non_places())
                    new_non_place.remove(j)
                    ordo = ordonnancement.Ordonnancement(flow_shop.nb_machines)
                    list_jobs = [flow_shop.get_job_by_id(i) for i in new_seq]
                    ordo.ordonnancer_liste_job(list_jobs)
                    new_val = flow_shop.calculer_borne_inf(ordo, new_seq)
                    new_num = s.numero() + 1
                    new_s = sommet.Sommet(new_seq, new_non_place, new_val, new_num)
                    if new_s.evaluation() < opt:
                        heapq.heappush(heap, new_s)

        print("La sequence optimale est : {}\n"
              "la duree est : {}".format(seq_opt, opt))
        return 0


if __name__ == "__main__":
    flow_shop = Flowshop()
    ordo = flow_shop.definir_par("jeu2.txt")
    ordo.afficher()
    start = datetime.now()
    liste_NEH = flow_shop.creer_liste_NEH()
    duree_NEH = datetime.now() - start
    duree_NEH = duree_NEH.total_seconds()
    liste_NEH.afficher()
    print()
    print("**********************************************")
    print("TEST EXO5")
    print("**** TEST DUREE DE DISPONOBILITE ***")
    print("La machine numéro ",
          2,
          " sera dispoible pour le job numéro ",
          flow_shop.get_job_by_id(2),
          " dans ",
          flow_shop.calculer_date_dispo(liste_NEH,
                                        2,
                                        flow_shop.get_job_by_id(2)),
          ' minutes')
    print()
    print("**** TEST DUREE LATENCE ****")
    print("Le job numéro ",
          flow_shop.get_job_by_id(2),
          "est à la machine",
          2,
          " et attendra ",
          flow_shop.calculer_duree_latence(liste_NEH,
                                           2,
                                           flow_shop.get_job_by_id(2)),
          " minutes avant de terminer")
    print()
    print("**** TEST DUREE DES JOBS ***")
    liste_jobs = [1, 2, 3]
    print("le temps d'execution des jobs ",
          liste_jobs,
          " sur la machine numéro ",
          2,
          "est égal à ",
          flow_shop.calculer_duree_jobs(4, liste_jobs))

    print()
    print("test brut", flow_shop.calculer_date_dispo(ordo, 2, flow_shop.get_job_by_id(3)))
    print("**** TEST DUREE DE LA VALEUR MINIMALE ***")
    LB = flow_shop.calculer_borne_inf(ordo, liste_jobs)
    print("La borne inférieure est égale à ", LB)

    print()
    print("**** TEST BRANCH & BOUND ***")
    start = datetime.now()
    flow_shop.evaluation_separation_()
    duree_B_and_B = datetime.now() - start
    duree_B_and_B = duree_B_and_B.total_seconds()
    print()
    print("L'heuristique NEH a duré : {} secondes\n"
          "le B&B a duré : {} secondes ".format(duree_NEH, duree_B_and_B))


