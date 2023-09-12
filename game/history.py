
from fundef import __ver__
from fundef import *
from structure import *
import time
sep=separacao()



def history():
    # player_name=getPlayerName()
    mensagem=['Você acorda em um lugar desconhecido\n',
              'Tu mal consegue enxergar...\n',
              'O que você faz?\n']
    confirmmensagem(mensagem,True)
    while True:#primeira parte
        Death00=False
        gritarDecision=False
        levantarDecision=False
        while True:
            pergunta('Gritar por ajuda','Se levantar',None)
            ultimateDecision00=resposta()
            if ultimateDecision00=='1':
                gritarDecision=True
                sepclear(1/4,0)
                break

            elif ultimateDecision00=='2':
                levantarDecision=True
                sepclear(1/4,0)
                break

            elif ultimateDecision00 in ['preguiça','preguica']:
                Death00=True
                sepclear(1/4,0)
                break
            else:
                sepclear(1/4,1)
                exibirmensagem(mensagem,True,0,False)
            
        if Death00==True:
            mensagem=['Você morreu.', 'Motivo da morte: ter estado com preguiça de se levantar.']
            confirmmensagem(mensagem,False)
            break
        elif gritarDecision==True:
                print(sep)
                DJpt('SOCORRO!!!!!!!!',20,1)
                DJpt(' ALGUÉM AÍ!!!!!!!!??????!!',30,1)
                linebreak(1)
                DJpt('...',1,0)
                mensagem=['Nada acontece.','A não ser...']
                exibirmensagem(mensagem,False,1,True)
                mensagem=['Pedras caem em sua direção!\n','Você consegue sair do buraco que você estava e dá graças a Deus que saiu a tempo.']
                confirmmensagem(mensagem,False)
                silentDecision_Grito=True
                break
    
        elif levantarDecision==True:
            print(sep)
            mensagem=['Você se levanta e se dá conta que está num buraco.\n',
                      'Tu consegue sair e vê pedras caindo em direção do buraco...\n',
                      'Era uma pessoa que as tinha jogado.']
            confirmmensagem(mensagem,False)
            break
          
        #     ultimateDecision00=input(f'1. Gritar por ajuda\n2. Se levantar\n\n-> ')
        #     sepclear(0)
        #     try:
        #         if ultimateDecision00==1:
        #             clearsep(0)
        #             DJpt(DJphrase='SOCORRO!!!!!!!!',DJtempo=20)
        #             time.sleep(1)
        #             DJpt(DJphrase=' ALGUÉM AÍ!!!!!!!!??????!!',DJtempo=30)
        #             print('\n')
        #             DJpt(DJphrase='...',DJtempo=1)
        #             print('Nada acontece.',end='',flush=True)
        #             time.sleep(1)
        #             print(f' A não ser',flush=True,end='')
        #             DJpt(DJphrase='...',DJtempo=20) 
        #             time.sleep(1)
        #             mensagem=['pedras caem em sua direção!','Você consegue fugir do buraco que você estava e dá graças a Deus que saiu a tempo.']
        #             confirmmensagem(mensagem)
        #             silentDecision_Grito=True
        #             morte00=False
        #             break
        #         elif ultimateDecision00==2:
        #             clearsep(0)
        #             mensagem=['Ao se levantar, tu percebe que está num buraco.',
        #                       'Com certa dificuldade por causa do sedentarismo, você sai dele.',
        #                       'E dá graças a Deus que ao sair você não foi esmagado por rochas que foram empurradas por alguém...']
        #             confirmmensagem(mensagem)
        #             silentDecision_Grito=False
        #             morte00=False
        #             print(sepbreak)
        #             break
        #         else:
        #             input(f'{sep}\nVocê morreu por ter feito nada, por pedras que desabaram.\n{sep}')
        #             morte00=True
        #             break
        #     except ValueError:
        #         continue
        # if morte00==False:
        #     input(f'\nContinua...\n{sep}')
        #     break
        # else: break

            # if morte00==False:
            #     input(f'Ao caminhar um pouco, você vê um corpo estirado no chão.\n\nContinua...\n{sep}')
            #     break
            # else: break
        

#         input('\nEntão tu percebe que é seu amigo.')
    
#         while True:
#             Fri00=input('\nEle é o... -> ')
            
#             if Fri00=='':
#                 input('\nEscreva o nome do seu amigo.')
#                 continue
#             else: break
#         input(f'\nO {Fri00} está desacordado. Então você pensa que há somente 3 opções...')
    
#         while True:
#             while True:
#                 Sep02_Decepcao=False   #    Decepção
#                 Sep03_Wakeup=False     #    Acordar
#                 Sep04_LeftBehind=False #    Abandono
#                 try:
#                     UDec01_Canibal=int(input('\n1. Comer de sua carne, por algum motivo\n2. Acordá-lo\n3. Deixá-lo desacordado e seguir em frente\n\n-> '))
#                     if UDec01_Canibal==1:
#                         Sep02_Decepcao=True
#                         Sep03_Wakeup=True
#                         break
#                     elif UDec01_Canibal==2:
#                         Sep03_Wakeup=True
#                         break
#                     elif UDec01_Canibal==3:
#                         Sep04_LeftBehind=True
#                         break
#                     else:input('\nFaça algo!')
#                 except ValueError:
#                     input('\nEscreva algum número!')
#                     continue
#             break
            
# #         if Sep02_Decepcao==True and Sep03_Wakeup==True:
# #                     input(f'\nAo tentar se aproximar e colocar a sua boca na sua perna, {Fri00} acorda e pergunta o que você está fazendo.')
# #                     input(f'\nVOCÊ ESTÁ TENTANDO ME COMER?! - {Fri00} grita desesperadamente')
# #                     while True:
#                         AC01=False # Brincadeirinha
#                         AC02=False # Putasso
#                         try:
#                             AC00=int(input('\n1. Me desculpe! Eu pensava que era uma coxinha de frango!\n2. CARALHO!?1 CÊ TÁ VIVO!?!\n\n-> '))
#                         except ValueError:
#                             input('\nEscreva algo.')
#                         if AC00==1:
#                             input('\nMANO!? É SÉRIO QUE TU TÁ DE BRINCADEIRINHA QUANDO A GENTE TÁ DESESPERADO?')
#                             input('\nBELEZA, NÉ? EU ESTOU PUTO PORQUE A MINHA PERNA AGORA ESTÁ DOENDO MUITO')
#                             AC01=True
#                             break
#                         elif AC00==2:
#                             input('\nÉ CLARO QUE EU TÔ!!! EU SÓ TAVA DESMAIADO POR CONTA DE ONTEM! O QUE TU ACHOU?!')
#                             input('\nBELEZA, NÉ? EU ESTOU PUTO PORQUE A MINHA PERNA AGORA ESTÁ DOENDO MUITO')
#                             AC02=True
#                             break
        
#         elif Sep03_Wakeup==True:
#             input(f'Com muito sono, {Fri00} acorda e tenta lembrar do que houve na noite passada.')
#             input(' ')
        
#         elif Sep04_LeftBehind==True: #  Abandonado
#             input('\nComo um belo amigo que você é, você o abandona e procura por uma saída dessa caverna.')
        
#         break
    
#     if Sep04_LeftBehind==False:
#         while True:
#             BA00=False #  Mentira
#             BA01=False #  Pergunta "brincaderinha"
#             BA03=False #  Pergunta "putasso"
        
#             if AC01==False:
#                 input('\nTu sabe como a gente chegou aqui? Eu não me lembro.')

#             elif AC01==True:
#                 input("\nTU  LEMBRA COMO QUE A GENTE CHEGOU AQUI? PELO MENOS TU SABE DISSO, NUM É?")
            
#             elif AC02==True:
#                 input('\nBELEZA, BELEZA! O QUE A GENTE FAZ AGORA? VOU TE COMER SE TU NÃO ME DER NENHUMA SUGESTÃO >:(')
#             while True:
#                 try:
#                     input('\n1. Como como')
#                 except ValueError:
#                     input('\nEscreva um número')
#     print(f'\n\n{Sep00_Grito} & {Sep04_LeftBehind}\n\n')
    
#     if Sep00_Grito==True and Sep04_LeftBehind==True:
#         DJphrase=f'\n\nEEEIII!!!! {name}!!!!'
#         DJtempo=30
#         fundef.DJpt(DJphrase,DJtempo)
#         DJphrase='\n\nEU PENSAVA QUE VOCÊ IA ME AJUDAR!'
#         DJtempo=30
#         fundef.DJpt(DJphrase,DJtempo)
        
        
#         while True:
#             UDec02_MORTO=int(input('\n1. Cara, eu pensava que tu já tava morto. Do que Adiantaria eu ver se tu tinha alguma coisa?\n2. Por que você tava no chão?'))
#             if UDec02_MORTO==1:
#                 DJphrase='\nÉ QUE EU PENSAVA QUE TU IA ME AJUDAR, DO QUE MAIS SERIA?!?!'
#                 DJtempo=30
#                 fundef.DJpt(DJphrase,DJtempo)
                
#     elif Sep00_Grito==False and Sep04_LeftBehind==True:
#         input('\nDepois de algum tempo você se depara com um pessoa, você não o conhece ele não parece ser agressivo.')
        
#     break
