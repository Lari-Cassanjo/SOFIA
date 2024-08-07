import requests
import buscas

from time import sleep
from datetime import datetime
import random
from os import system
system('cls')

api_key = 'a8b56b86a83dee254fadcaf769bd55dc'

usuario = 'Larissa'

print('~'*80)
print('{:^80}'.format('S.O.F.I.A.'))
print('~'*80)

hora = datetime.now().time()
#hora = hora.strftime('%H:%M') #Foramatando para apenas horas e minutos
hora = hora.strftime('%H')
hora = int(hora)

if hora >= 6 and hora < 12:
    cumprimento = 'Bom dia'
elif hora >= 12 and hora < 18:
    cumprimento = 'Boa tarde' 
elif hora >=18 and hora < 23:
    cumprimento = 'Boa noite'
else:
    cumprimento = 'Já está tarde'
    
print(f'{cumprimento}, Lari!')
sleep(1)
print('Como quer escolher o filme de hoje?')
print('1- Gênero \n2- Atriz/Ator \n3- Diretor(a)  \n4- Completamente Aleatório')
sleep(1)

selecao = 0
while selecao != 1 or selecao != 2 or selecao != 3 or selecao != 4:
    selecao = int(input('Seletor: '))
    print('-'*60)
    if selecao == 1:
        print('Ótimo. Primeiro preciso saber o gênero de filme que quer ver.')
        escolha = 0
        while escolha != 1 or escolha != 2:
            escolha = int(input('Gostaria de digitar (1) ou que eu escolha para você (2)? '))
            if escolha == 1:
                genero = input('Digite o gênero de filme que quer ver: ')
                genero_id = buscas.buscar_genero_id(genero, api_key)
                if genero_id:
                    filmes = buscas.buscar_filmes_por_genero(genero_id, api_key)
                    if filmes:
                        filme = random.choice(filmes)
                    print(f'Filme do gênero {genero}: {filme['title']}, {filme['release_date'][:4]}')
                else:
                    print("Gênero não encontrado.")
                break
            elif escolha == 2:
                generos = buscas.buscar_generos(api_key)
                if generos:
                    genero = random.choice(generos)
                    genero_id = genero['id']
                    genero_nome = genero['name']
                    
                    filmes = buscas.buscar_filmes_por_genero(genero_id, api_key)
                    if filmes:
                        filme = random.choice(filmes)
                        print(f'Filme do gênero {genero['name']}: {filme['title']}, {filme['release_date'][:4]}')
                else:
                    print("Não foi possível obter a lista de gêneros.")
                break
            else:
                print('Escolha inválida!')
        break
    elif selecao == 2:
        print('Qual a atriz ou ator que você quer ver hoje?')
        nome_ator = input('- ')
        ator_id = buscas.buscar_ator_id(nome_ator, api_key)
        if ator_id:
            filmes = buscas.buscar_filmes_por_ator(ator_id, api_key)
            if filmes:
                filme_aleatorio = random.choice(filmes)
                print(f"Filme: {filme_aleatorio['title']}, {filme_aleatorio['release_date'][:4]}")
            else:
                print(f"Nenhum filme encontrado para {nome_ator}.")
        else:
            print(f"Ator/Atriz {nome_ator} não encontrado(a).")
        break
    elif selecao == 3:
        print('Qual a diretora ou diretor que você quer assitir hoje?')
        nome_diretor = input('- ')
        diretor_id = buscas.buscar_diretor_id(nome_diretor,api_key)
        if diretor_id:
            filmes = buscas.buscar_filme_por_diretor(diretor_id,api_key)
            if filmes:
                filme_aleatorio = random.choice(filmes)
                print(f'Filme: {filme_aleatorio['title']}, {filme_aleatorio['release_date'][:4]}')
            else:
                print(f'Nenhum filme encontrado para {nome_diretor}.')
        else:
            print(f'{nome_diretor} não encontrada(o)!')
        break
    elif selecao == 4:
        pagina_aleatoria = random.randint(1, 500)
        filmes = buscas.obter_filmes_da_pagina(api_key, pagina_aleatoria)
        if filmes:
            filme_aleatorio = random.choice(filmes)
            filme_id = filme_aleatorio['id']
            detalhes = buscas.obter_detalhes_do_filme(api_key, filme_id)
            creditos = buscas.obter_elenco_e_equipe(api_key, filme_id)
            diretor = None
            for membro in creditos['crew']:
                if membro['job'] == 'Director':
                    diretor = membro['name']
            elenco = [ator['name'] for ator in creditos['cast'][:5]]
            sinopse = detalhes['overview']
            print(f"Filme: {filme_aleatorio['title']}, {filme_aleatorio['release_date'][:4]} - {diretor}")
            print('-'*20)
            print('\033[33mElenco Principal:\033[m')
            print(f'{'\n'.join(elenco)}')
            print('-'*10)
            print('\033[33mSinopse:\033[m')
            print(f'{sinopse}')
        else:
            print("Nenhum filme encontrado.")
        break
    else:
        print('Seleção Inválida')

print('-'*60)
print('Aproveite o filme!')
