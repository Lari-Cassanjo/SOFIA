from imdb import Cinemagoer, IMDbError

from random import randint
from os import system
system('cls')

# create an instance of the Cinemagoer class
ia = Cinemagoer()

#Mostrar pessoa:
pessoa = ia.search_person('julia roberts')
print(pessoa[0])
julia = pessoa[0].personID
print(julia)

#Procurar filme por gênero
movies = ia.search_keyword('romance')
print(len(movies))
movies = movies[0]
choice = ia.get_keyword(movies)
print(len(choice))
