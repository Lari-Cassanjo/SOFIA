import requests #Para conseguir fazer a solicitação HTTP

from random import randint
from os import system
system('cls')
api_key = 'a8b56b86a83dee254fadcaf769bd55dc' #Deixando mais fácil o uso da chave da API

# Função para buscar o ID do gênero pelo nome
def buscar_genero_id(nome_genero, api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    for genero in data['genres']:
        if genero['name'].lower() == nome_genero.lower():
            return genero['id']
    return None

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
nome_genero = "Romance"
genero_id = buscar_genero_id(nome_genero, api_key)
if genero_id:
    filmes = buscar_filmes_por_genero(genero_id, api_key)
    for filme in filmes:
        print(f"Titulo: {filme['title']}, Ano: {filme['release_date'][:4]}, TMDb ID: {filme['id']}")
else:
    print("Gênero não encontrado.")