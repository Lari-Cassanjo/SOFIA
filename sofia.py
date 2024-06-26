from imdb import Cinemagoer

from time import sleep
from datetime import datetime
from os import system
system('cls')

# create an instance of the Cinemagoer class
ia = Cinemagoer()

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
print('Como quer esccolher o filme de hoje?')
print('1- Gênero \n2- Atriz/Ator \n3- Diretor(a)')
sleep(1)

selecao = 0
while selecao != 1 or selecao != 2 or selecao != 3:
    selecao = int(input('Seletor: '))
    if selecao == 1:
        print('Ótimo. Primeiro preciso saber o gênero de filme que quer ver.')
        escolha = 0
        while escolha != 1 or escolha != 2:
            escolha = int(input('Gostaria de digitar (1) ou que eu escolha para você (2)?'))
            if escolha == 1:
                genero = input('Digite o gênero de filme que quer ver: ')
                break
            elif escolha == 2:
                genero = 'random'
                break
            else:
                print('Escolha inválida!')
        #teste
        print(f'Filme do gênero {genero}.')
        break
    elif selecao == 2:
        print('Qual a atriz ou ator que você quer ver hoje?')
        atriz = input('- ')
        #teste
        print(f'Filme com a(o) {atriz}.')
        break
    elif selecao == 3:
        print('Qual a diretora ou diretor que você quer assitir hoje?')
        diretora = input('- ')
        #teste
        print(f'Filme com a(o) {diretora}.')
        break
    else:
        print('Seleção Inválida')

print('Aproveite o filme!')
    