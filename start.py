##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.

import time
input('\nPressione Enter para jogar Cave Game.\n')


Tu00=input(f'deseja ver o tu')
Tu01=time.sleep(5)
if Tu00==():
    input('é bem fácil')
    
input('\nVocê acordou numa caverna...\n')
input('\nTu mal consegue enxergar...\n')
input('\nO que você faz?\n')


while True:
    while True:
        A02=False
        try:
            A01=int(input('\n1. Grito por ajuda\n2. Se levantar\n\n-> '))
            if A01==1: input('\nNada acontece.')
            elif A01==2:
                print('\nPedras desabaram depois que você se levantou...\n')
                A02=True
                break
            else:
                input('Você morreu por pedras que cairam.')
                break
        except ValueError:
            input('\nEscreva um número.\n')
            continue
    if A02==True:print('\nEra seu amigo.\n')
    else:break
    
    break
input('Esse foi o Cave Game! Espero que tenha gostado!')
input('Programador: pensa')