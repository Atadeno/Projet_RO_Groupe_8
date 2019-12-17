#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:50:17 2019

@author: jojo
"""

import random


#appariement de manière aléatoire
def rand_pairing(L) :
	n = int(len(L)/2)
	M = []
	for k in range(n):
		index = random.randint(1, len(L)-1)
		M.append(L[0])
		M.append(L[index])
		L.pop(index)
		L.pop(0)
	L = M
	print(L)
	

#apariement par ordre croissant des Cmax
def C_pairing(L):
	L = sorted(L, key = lambda colonnes: colonnes[1])
	print(L)
	

#On peut aussi prendre la liste telle quelle



