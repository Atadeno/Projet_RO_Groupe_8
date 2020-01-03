#!/usr/bin/env python

""" Classe Ordonnancement """
import itertools

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019'

import job


class Ordonnancement():

	# constructeur pour un ordonnancement vide
	def __init__(self, nb_machines):
		# séquence des jobs
		self.seq = []
		self.nb_machines = nb_machines
		# durée totale
		self.dur = 0
		# date à partir de laquelle la machine est libre
		self.date_dispo = [0 for i in range(self.nb_machines)]

	def to_index(self):
		L = []
		for job in self.seq:
			L.append(job.numero())
		return L

	def duree(self):
		return self.dur

	def sequence(self):
		return self.seq

	def date_disponibilite(self,
						   num_machine):
		return self.date_dispo[num_machine]

	def date_debut_operation(self,
							 job, operation):
		return job.date_deb[operation]

	def fixer_date_debut_operation(self,
								   job,
								   operation,
								   date):
		job.date_deb[operation] = date

	def afficher(self):
		print("Ordre des jobs :", end='')
		for job in self.seq:
			print(" ", job.numero(), " ", end='')
		print()
		for job in self.seq:
			print("Job", job.numero(), ":", end='')
			for mach in range(self.nb_machines):
				print(" op", mach, "à t =", self.date_debut_operation(job, mach), "|", end='')
			print()
		print("Durée ordo =", self.dur)

	# exo 2 A REMPLIR
	def ordonnancer_job(self, new_job):
		if not(new_job in self.seq):
			self.seq.append(new_job)
			self.fixer_date_debut_operation(new_job, 0, self.date_dispo[0])
			self.date_dispo[0] = self.date_dispo[0] + new_job.duree_op[0]
			for i in range(1, self.nb_machines):
				date_ajout = max(self.date_dispo[i], self.date_dispo[i - 1])
				self.fixer_date_debut_operation(new_job, i, date_ajout)
				self.date_dispo[i] = date_ajout + new_job.duree_op[i]
			self.dur = self.date_dispo[self.nb_machines - 1]
			#print("job ", job.num, " a été ordonnancé")
	# exo 3 A REMPLIR
	def ordonnancer_liste_job(self, liste_jobs):
		for job in liste_jobs:
			self.ordonnancer_job(job)



if __name__ == "__main__":
	job1 = job.Job(1, [3, 2, 4, 2, 1])
	job2 = job.Job(2, [2, 5, 2, 1, 4])
	job3 = job.Job(3, [1, 2, 10, 4, 7])
	print(job1)
	List_Job = [job1, job2, job3, job1]

	ordo = Ordonnancement(5)
	ordo.ordonnancer_liste_job(List_Job)

	ordo.afficher()
	print("ordo.date_dispo[0]=", ordo.date_dispo[0])
	print("job1.duree_job=", job1.duree_job)
	print("ordo.date_dispo[1]=", ordo.date_dispo[1])
	print("job2.duree_job=", job2.duree_job)
	print(ordo.to_index())
	ordo.afficher()

	pass
