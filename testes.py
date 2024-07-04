import requests #Para conseguir fazer a solicitação HTTP

import random
from os import system
system('cls')
api_key = 'a8b56b86a83dee254fadcaf769bd55dc' #Deixando mais fácil o uso da chave da API

# Função para obter filmes de uma página específica
def obter_filmes_da_pagina(api_key, pagina):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&page={pagina}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return data['results']
    else:
        return []
    
# Exemplo de uso
pagina_aleatoria = random.randint(1, 500)
print(pagina_aleatoria)
filmes = obter_filmes_da_pagina(api_key, pagina_aleatoria)
if filmes:
    filme_aleatorio = random.choice(filmes)
    print(f"Filme escolhido aleatoriamente:")
    print(f"Titulo: {filme_aleatorio['title']}, Ano: {filme_aleatorio['release_date'][:4]}, TMDb ID: {filme_aleatorio['id']}")
else:
    print("Nenhum filme encontrado.")
