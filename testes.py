import requests #Para conseguir fazer a solicitação HTTP

import random
from os import system
system('cls')
api_key = 'a8b56b86a83dee254fadcaf769bd55dc' #Deixando mais fácil o uso da chave da API

# Função para buscar a lista de gêneros
def buscar_generos(api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    if 'genres' in data:
        return data['genres']
    else:
        return []

# Função para buscar filmes por gênero
def buscar_filmes_por_genero(genero_id, api_key):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genero_id}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return data['results']
    else:
        return []

# Exemplo de uso
generos = buscar_generos(api_key)
if generos:
    genero_escolhido = random.choice(generos)
    genero_id = genero_escolhido['id']
    genero_nome = genero_escolhido['name']
    
    print(f"Gênero escolhido aleatoriamente: {genero_nome}")
    
    filmes = buscar_filmes_por_genero(genero_id, api_key)
    for filme in filmes:
        print(f"Titulo: {filme['title']}, Ano: {filme['release_date'][:4]}, TMDb ID: {filme['id']}")
else:
    print("Não foi possível obter a lista de gêneros.")