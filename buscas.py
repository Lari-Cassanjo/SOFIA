import requests #Para conseguir fazer a solicitação HTTP

from os import system
system('cls')

api_key = 'a8b56b86a83dee254fadcaf769bd55dc' #Deixando mais fácil o uso da chave da API

def buscar_generos(api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    if 'genres' in data:
        return data['genres']
    else:
        return []

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

# Função para buscar o ID do ator/atriz pelo nome
def buscar_ator_id(nome_ator, api_key):
    url = f"https://api.themoviedb.org/3/search/person?api_key={api_key}&query={nome_ator}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and data['results']:
        return data['results'][0]['id']
    else:
        return None

# Função para buscar filmes do ator/atriz pelo ID
def buscar_filmes_por_ator(ator_id, api_key):
    url = f"https://api.themoviedb.org/3/person/{ator_id}/movie_credits?api_key={api_key}&language=pt-BR"
    response = requests.get(url)
    data = response.json()
    if 'cast' in data:
        return data['cast']
    else:
        return []