import random

### Appariement ###

# Une liste de N individus à apparier. L'appariement est aléatoire dans un premier temps
# Les individus n et n+1 seront croisés dans la suite
# Il suffit juste de mélanger la liste dans ce cas

def appariement_population(population):
    random.shuffle(population)
