import requests #Para conseguir fazer a solicitação HTTP

import random
from os import system
system('cls')
api_key = 'a8b56b86a83dee254fadcaf769bd55dc' #Deixando mais fácil o uso da chave da API

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

# Exemplo de uso
nome_ator = "Marisa Orth"
ator_id = buscar_ator_id(nome_ator, api_key)
if ator_id:
    filmes = buscar_filmes_por_ator(ator_id, api_key)
    print(len(filmes))
    if filmes:
        filme_aleatorio = random.choice(filmes)
        print(f"Filme escolhido aleatoriamente:")
        print(f"Titulo: {filme_aleatorio['title']}, Ano: {filme_aleatorio['release_date'][:4]}, TMDb ID: {filme_aleatorio['id']}")
    else:
        print(f"Nenhum filme encontrado para {nome_ator}.")
else:
    print(f"Ator/Atriz {nome_ator} não encontrado(a).")