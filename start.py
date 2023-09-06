##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.

import time
input('\nPressione Enter para jogar Cave Game.')


input('\nVocê acordou numa caverna...')
input('\nTu mal consegue enxergar...')
input('\nO que você faz?')


while True:
    while True:
        A02=False
        try:
            A01=int(input('\n1. Grito por ajuda\n2. Se levantar -> '))
            if A01==1: input('\nNada acontece.')
            elif A01==2:
                input('\nPedras desabaram depois que você se levantou...')
                A02=True
                break
            else:
                input('Você morreu por ter feito nada, por pedras que desabaram.')
                break
        except ValueError:
            input('\nEscreva um número.')
            continue
    if A02==True:input('\nE você vê, na total escuridão um corpo.')
    else:break
    
    input('\nEntão tu percebe que é seu amigo')
    
    while True:
        f00=input('\nO seu nome é... -> ')
        
        if f00=='':
            input('Escreva algo.')
            continue
        else: break
    input(f'\nO {f00} está desacordado. Você tem 3 opções...')
    
    while True:
        AB01=False
        AB02=False
        AB03=False
        AB04=False
        try:
            A00=int(input('\n1. Comer de sua carne\n2. O acordar\n3. Deixá-lo desacordado e seguir em frente'))
            if A00==1:
                AB01=True
                AB02=True
            elif A00==2:
                AB03==True
            elif A00==3:
                AB04==True
            else:input('Faça algo!')
        except ValueError:
            input('\nEscreva algum número!')
            continue
                
    break
input('Esse foi o Cave Game! Espero que tenha gostado!')
input('Programador: pensa')

