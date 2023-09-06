##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.

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
        AB01=False #    Decepção
        AB02=False #    Acordar
        AB03=False #    Deixá-lo
        try:
            AB00=int(input('\n1. Comer de sua carne, porque você está drogado\n2. O acordar\n3. Deixá-lo desacordado e seguir em frente'))
            if AB00==1:
                AB01=True
                AB02=True
                break
            elif AB00==2:
                AB02=True
                break
            elif AB00==3:
                AB03=True
                break
            else:input('Faça algo!')
        except ValueError:
            input('\nEscreva algum número!')
            continue
        
        if AB01==True and AB02==True:
            input(f'\nAo tentar se aproximar e colocar a sua boca na sua perna, {f00} acorda e pergunta o que você está fazendo.')
            input(f'\nVOCÊ ESTÁ TENTANDO ME COMER?! - {f00} grita desesperadamente')
            while True:
                try:
                    AC00=int(input('\n1. Me desculpe! Eu pensava que era uma coxinha de frango!\n2. CARALHO!?1 CÊ TÁ VIVO!?!\n3. Eu pensava que você está morto e para eu sobreviver eu precisava consumir você.\n-> '))
                except ValueError:
                    input('\nEscreva algo.')
                if AC00==1:
                    input('\nMANO!? É SÉRIO QUE TU TÁ DE BRINCADEIRINHA QUANDO A GENTE TÁ NUMA CAVERNA QUE A GENTE MAL SE LEMBRA COMO QUE A GENTE CHEGOU AQUI?')
                    break
                elif AC00==2:
                    input('\nÉ CLARO QUE EU TÔ!!! EU SÓ TAVA DESMAIADO POR CONTA DE ONTEM! O QUE TU ACHOU?!')
                    AC01=True
                elif AC00==3:
                    input('\nQuê? O que você tá falando? Só deve ter passado uns 2 dias... né?')
                    AC02=True
                    break
            

    break
input('Esse foi o Cave Game! Espero que tenha gostado!')
input('Programador: pensa')

