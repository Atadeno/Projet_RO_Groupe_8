import random

### Appariement ###

# Une liste de N individus à apparier. L'appariement est aléatoire dans un premier temps
# Les individus n et n+1 seront croisés dans la suite
# Il suffit juste de mélanger la liste dans ce cas

def appariement_population(population):
	random.shuffle(population)
	
	
	
#On fait un appariement par valeur de Cmax croissant
def C_pairing(L):
	pass
	#L = sorted(L, key = lambda colonnes: colonnes[1])


def pairing(L):
	#L = sorted(L, key = lambda colonnes: colonnes[1])
	n = int(len(L)/2)
	M=[]
	for k in range(n):
		M.append([L[k], L[k+n]])
	L = M
	
	
#on apparie le Cmax minimal avec le maximal
def mixed_pairing(L):
	#L = sorted(L, key = lambda colonnes: colonnes[1])
	m = len(L)
	n = int(m/2)
	M=[]
	for k in range(n):
		M.append([L[k], L[m-k-1]])
	L = M
