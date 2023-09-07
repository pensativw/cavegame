##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.
import time

input('\nPressione Enter para jogar Cave Game.')

input('\nAntes de tudo, qual é o seu nome?') #incompleto

x = range(3, 6)
for n in x:
    print(n)
    time.sleep(3)
input('\nVocê acabou de acordar')
input('\nTu mal consegue enxergar...')
input('\nO que você faz?')


while True:
    while True:
        A02=False
        try:
            A01=int(input('\n1. Gritar por ajuda\n2. Se levantar\n\n-> '))
            if A01==1:
                print('\nSOCORRO!!!')
                time.sleep(3)
                print('\nALGUÉM AÍ!!!!??')
                time.sleep(3)
                input('\nNada acontece.')
                A00=True
            elif A01==2:
                input('\nTu percebe que está num buraco, e sai daquele buraco.')
                input('\nE dá graças a Deus que ao sair você não foi esmagado por rochas que acabaram de ser empurradas por alguém...')
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
            input('\nEscreva o nome do seu amigo.')
            continue
        else: break
    input(f'\nO {f00} está desacordado. Você tem 3 opções...')
    
    while True:
        while True:
            AB01=False #    Decepção
            AB02=False #    Acordar
            AB03=False #    Abandono
            try:
                AB00=int(input('\n1. Comer de sua carne, por algum motivo\n2. O acordar\n3. Deixá-lo desacordado e seguir em frente\n\n-> '))
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
            input(f'Com muito sono, {f00} acorda e tenta lembrar do que houve na noite passada.')
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

            elif AC01==True:
                input("\nTU  LEMBRA COMO QUE A GENTE CHEGOU AQUI? PELO MENOS TU SABE DISSO, NUM É?")
            
            elif AC02==True:
                input('\nBELEZA, BELEZA! O QUE A GENTE FAZ AGORA? VOU TE COMER SE TU NÃO ME DER NENHUMA SUGESTÃO >:(')
            while True:
                try:
                    input('\n1. Como como')
                except ValueError:
                    input('\nEscreva um número')
                    
    elif AB03==True and A00==True:
        input('EI!')
        time.sleep(2)
        input('Você ')
        while True:
            input('1. Não')
    
    break
input('\nEsse foi o Cave Game! Espero que tenha gostado!')
input('\nProgramador: pensa')

