##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.

ver='\n0.0.2.6'

import time
from fundef import DJpt,TUTO

input('\nPressione Enter para jogar Cave Game.')

TUTO()  

while True:
    name = input('\nEscreva seu nome -> ') 
    if name=='ver':
        print(ver)
        continue
    else:
        break
        
    
while name.strip() == '' :
    print('\nEscreva algo.',end=' ')
    time.sleep(1)
    name = input('Nome -> ')

input('\nVocê acorda em um lugar desconhecido')
input('\nTu mal consegue enxergar...')
input('\nO que você faz?')


while True:
    while True:
        Det00=True
        try:
            UDec00=int(input('\n1. Gritar por ajuda\n2. Se levantar\n\n-> '))
            Dec00=False
            if UDec00==1:
                DJtempo=20
                DJphrase='\nSOCORRO!!!!!!'
                DJpt(DJphrase,DJtempo)
                DJtempo=20
                DJphrase='\n\nALGUÉM AÍ?!?!?!?!?!\n\n'
                DJpt(DJphrase,DJtempo)
                DJtempo=2
                DJphrase='...'
                DJpt(DJphrase,DJtempo)
                input(' Nada acontece.')
                Dec00=True
            elif UDec00==2:
                input('\nAo se levantar, tu percebe que está num buraco.')
                input('\nCom certa dificuldade por causa do sedentarismo, você sai dele.')
                input('\nE dá graças a Deus que ao sair você não foi esmagado por rochas que foram empurradas por alguém...')
                Det00=False
                break
            else:
                input('\nVocê morreu por ter feito nada, por pedras que desabaram.')
                break
        except ValueError:
            input('\nEscreva um número.')
            continue
    if Det00==False:input('\nAo caminhar um pouco, você vê um corpo estirado no chão.')
    else:break
    
    input('\nEntão tu percebe que é seu amigo.')
    
    while True:
        Fri00=input('\nEle é o... -> ')
        
        if Fri00=='':
            input('\nEscreva o nome do seu amigo.')
            continue
        else: break
    input(f'\nO {Fri00} está desacordado. Então você pensa que há somente 3 opções...')
    
    while True:
        while True:
            Sep00_Decepcao=False #    Decepção
            Sep01_Wakeup=False #    Acordar
            Sep02_LeftBehind=False #    Abandono
            try:
                UDec01_Canibal=int(input('\n1. Comer de sua carne, por algum motivo\n2. Acordá-lo\n3. Deixá-lo desacordado e seguir em frente\n\n-> '))
                if UDec01_Canibal==1:
                    Sep00_Decepcao=True
                    Sep01_Wakeup=True
                    break
                elif UDec01_Canibal==2:
                    Sep01_Wakeup=True
                    break
                elif UDec01_Canibal==3:
                    Sep02_LeftBehind=True
                    break
                else:input('\nFaça algo!')
            except ValueError:
                input('\nEscreva algum número!')
                continue
        
        if Sep00_Decepcao==True and Sep01_Wakeup==True:
                    input(f'\nAo tentar se aproximar e colocar a sua boca na sua perna, {Fri00} acorda e pergunta o que você está fazendo.')
                    input(f'\nVOCÊ ESTÁ TENTANDO ME COMER?! - {Fri00} grita desesperadamente')
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
        
        elif Sep01_Wakeup==True:
            input(f'Com muito sono, {Fri00} acorda e tenta lembrar do que houve na noite passada.')
            input(' ')
        
        elif Sep02_LeftBehind==True: #  Abandonado
            input('\nComo um belo amigo que você é, você o abandona e procura por uma saída dessa caverna.')
        
        break
    
    if Sep02_LeftBehind==False:
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
                    
    elif Sep02_LeftBehind==True and Dec00==True:
        DJphrase=f'\nEEEIII!!!! {name}!!!!'
        DJtempo=30
        DJpt(DJphrase,DJtempo)
        
        DJphrase='\nEU PENSAVA QUE VOCÊ IA ME AJUDAR!'
        DJtempo=30
        DJpt(DJphrase,DJtempo)
        while True:
            UDec02_MORTO=int(input('\n1. Cara, eu pensava que tu já tava morto. Do que Adiantaria eu ver se tu tinha alguma coisa?\n2. Por que você tava no chão?'))
            if UDec02_MORTO==1:
                DJphrase='\nÉ QUE EU PENSAVA QUE TU IA ME AJUDAR, DO QUE MAIS SERIA?!?!'
                DJtempo=30
                DJpt(DJphrase,DJtempo)
                
    elif Sep02_LeftBehind==True and Dec00==False:
        input('\nDepois de algum tempo você se depara com um pessoa, você não o conhece ele não parece ser agressivo.')
        
    break
input('\nEsse foi o Cave Game! Espero que tenha gostado!')
input('\nProgramador: pensa')

