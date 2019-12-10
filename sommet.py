#!/usr/bin/env python

""" Classe Sommet :

A utiliser avec une file de priorité (heapq)
pour la recherche arborescente de la méthode
par évaluation-séparation
"""
import heapq
import flowshop
import copy
import ordonnancement

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019'


class Sommet():

    def __init__(self, seq, non_places, val, num):
        self.seq = seq
        self.non_places = non_places
        self.val = val
        self.num = num

    def __str__(self):
        ch = ''
        ch = ch + 'Numero du sommet : {} sequencement : {} non_placés : {}, valeur : {} '.format(self.num, self.seq,
                                                                                                 self.non_places,
                                                                                                 self.val)
        return ch

    def sequence(self):
        return self.seq

    def jobs_non_places(self):
        return self.non_places

    def evaluation(self):
        return self.val

    def numero(self):
        return self.num

    def __lt__(self, autre):
        """ Etablit la comparaison selon l'évaluation associée au sommet """
        return self.val < autre.val


if __name__ == "__main__":
    flow_shop = flowshop.Flowshop()
    ordo = flow_shop.definir_par("jeu3.txt")
    liste_NEH = flow_shop.creer_liste_NEH()
    #liste = [3, 2, 0, 1]
    liste = ordo.to_index()
    val = flow_shop.calculer_borne_inf(ordo, liste)
    s = Sommet([], liste, val, 0)
    heap = []
    heapq.heappush(heap, s)
    opt = 1000000
    seq_opt = []

    while len(heap) != 0:
        s = heapq.heappop(heap)
        print(s)
        if len(s.jobs_non_places()) == 0:
            ordo = ordonnancement.Ordonnancement(flow_shop.nb_machines)
            list_jobs = [flow_shop.get_job_by_id(i) for i in s.sequence()]
            ordo.ordonnancer_liste_job(list_jobs)
            if ordo.duree() <= opt:
                opt = ordo.duree()
                seq_opt = s.sequence()
        else:
            for j in s.jobs_non_places():
                new_seq = copy.deepcopy(s.sequence()) + [j]
                new_non_place = copy.deepcopy(s.jobs_non_places())
                new_non_place.remove(j)
                ordo = ordonnancement.Ordonnancement(flow_shop.nb_machines)
                list_jobs = [flow_shop.get_job_by_id(i) for i in new_seq]
                ordo.ordonnancer_liste_job(list_jobs)
                ordo.afficher()
                new_val = flow_shop.calculer_borne_inf(ordo, new_seq)
                new_num = s.numero() + 1
                new_s = Sommet(new_seq, new_non_place, new_val, new_num)
                if new_s.evaluation() < opt:
                    heapq.heappush(heap, new_s)

    print("La sequence optimale est : {}\n"
          "la duree est : {}".format(seq_opt, opt))