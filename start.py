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
            A01=int(input('\n1. Grito por ajuda\n2. Se levantar\n\n-> '))
            if A01==1: input('\nNada acontece.')
            elif A01==2:
                input('\nPedras desabaram depois que você se levantou...')
                A02=True
                break
            else:
                input('\nVocê morreu por ter feito nada, por pedras que desabaram.')
                break
        except ValueError:
            input('\nEscreva um número.')
            continue
    if A02==True:input('\nE você vê, na total escuridão um corpo.')
    else:break
    
    input('\nEntão tu percebe que é seu amigo')
    
    while True:
        f00=input('\nEle é o... -> ')
        
        if f00=='':
            input('\nEscreva o seu nome.')
            continue
        else: break
    input(f'\nO {f00} está desacordado. Você tem 3 opções...')
    
    while True:
        while True:
            AB01=False #    Decepção
            AB02=False #    Acordar
            AB03=False #    Abandono
            try:
                AB00=int(input('\n1. Comer de sua carne, porque você está drogado\n2. O acordar\n3. Deixá-lo desacordado e seguir em frente\n\n-> '))
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
                else:input('\nFaça algo!')
            except ValueError:
                input('\nEscreva algum número!')
                continue
        
        if AB01==True and AB02==True:
                    input(f'\nAo tentar se aproximar e colocar a sua boca na sua perna, {f00} acorda e pergunta o que você está fazendo.')
                    input(f'\nVOCÊ ESTÁ TENTANDO ME COMER?! - {f00} grita desesperadamente')
                    while True:
                        AC01=False # Brincadeirinha
                        AC02=False # Putasso
                        try:
                            AC00=int(input('\n1. Me desculpe! Eu pensava que era uma coxinha de frango!\n2. CARALHO!?1 CÊ TÁ VIVO!?!\n\n-> '))
                        except ValueError:
                            input('\nEscreva algo.')
                        if AC00==1:
                            input('\nMANO!? É SÉRIO QUE TU TÁ DE BRINCADEIRINHA QUANDO A GENTE TÁ DESESPERADO?')
                            input('\nBELEZA, NÉ? EU ESTOU PUTO PORQUE A MINHA PERNA AGORA ESTÁ DOENDO MUITO')
                            AC01=True
                            break
                        elif AC00==2:
                            input('\nÉ CLARO QUE EU TÔ!!! EU SÓ TAVA DESMAIADO POR CONTA DE ONTEM! O QUE TU ACHOU?!')
                            input('\nBELEZA, NÉ? EU ESTOU PUTO PORQUE A MINHA PERNA AGORA ESTÁ DOENDO MUITO')
                            AC02=True
                            break
        
        elif AB02==True:
            input(f'Com muito sono, {f00} acorda e tenta lembrar a você o que aconteceu na noite passada.')
            input(' ')
        
        elif AB03==True: #  Abandonado
            input('\nComo um belo amigo que você é, você o abandona e procura por uma saída dessa caverna.')
        
        break
    
    if AB03==False:
        while True:
            BA00=False #  Mentira
            BA01=False #  Pergunta "brincaderinha"
            BA03=False #  Pergunta "putasso"
        
            if AC01==False:
                input('\nTu sabe como a gente chegou aqui? Eu não me lembro.')
                while True:
                    try:
                        input('\n1. Não\n2. Mentir')
                    except ValueError:
                        input('\nEscreva um número.')
            elif AC01==True:
                input("\nTU  LEMBRA COMO QUE A GENTE CHEGOU AQUI? PELO MENOS TU SABE DISSO, NUM É?")
    
    else:input('\nVocê é um belo de um filha da puta.')
    
    break
input('\nEsse foi o Cave Game! Espero que tenha gostado!')
input('\nProgramador: pensa')

