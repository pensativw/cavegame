
from fundef import __ver__
from fundef import *
from structure import *
import time



def history():
    player_name=getPlayerName()
    isDead=False
    while not isDead:
        mensagem=['Você acorda em um lugar desconhecido\n',
                  'Tu mal consegue enxergar...\n',
                  'O que você faz?\n']
        confirmmensagem(mensagem,True)
        gritarDecision=False
        levantarDecision=False
        while True:
            pergunta('Gritar por ajuda','Se levantar',None)
            ultimateDecision00=resposta()

            if ultimateDecision00=='1':
                gritarDecision=True
                breaksep('end',1,1/4)
                break

            elif ultimateDecision00=='2':
                levantarDecision=True
                breaksep('end',1,1/4)
                break

            elif ultimateDecision00 in ['preguiça','preguica']:
                isDead=True
                DeathMessage='Por ter tido preguiça num dos momentos mais importantes.'
                
                breaksep('padrao')
                break
            else:
                print(sep())
                print('Escreva algo!')
                clear(1/4)
                print(sep())
                exibirmensagem(mensagem,True,0,False)
        if gritarDecision==True:
                print(sep())
                DJpt('SOCORRO!!!!!!!!',20,1)
                DJpt(' ALGUÉM AÍ!!!!!!!!??????!!',30,1)
                breakline(1)
                DJpt('...',1,0)
                mensagem=['Nada acontece.','A não ser...']
                exibirmensagem(mensagem,False,1,True)
                mensagem=['Pedras caem em sua direção!\n','Você consegue sair do buraco onde você estava e dá graças a Deus que saiu a tempo.']
                confirmmensagem(mensagem,False)
                silentDecision_Grito=True
                breaksep('end',1,1/4)
                break

        elif levantarDecision==True:
            mensagem=['Você se levanta e se dá conta que está num buraco.\n',
                      'Tu consegue sair e vê pedras caindo em sua direção...\n',
                      'Foi alguém que as jogou.']
            confirmmensagem(mensagem,True)
            silentDecision_Levantar=True
            breaksep('padrao')
            break
    while not isDead:
        mensagem=['Ao caminhar um pouco, você encontra um corpo estirado no chão.\n',
                'Era o seu amigo, que só estava desmaiado...']
        confirmmensagem(mensagem,True)
        breaksep('padrao')
        friend00=getFriend00()
        # player_name='Maurício'
        breaksep('start')
        DJpt('CARALHO!',30,1)
        DJpt(f' {friend00}!!!!'.upper(),30,1)
        DJpt(f' CÊ TÁ BEM?!',30,1,player_name)
        sep(1)
        DJpt(f'{player_name[:3]}...',5,1,friend00)
        breakline(1)
        mensagem='Ele foi baleado na perna e parece que está perdendo a consciência.'
        confirmmensagem(mensagem,False)
        break

    if isDead:
        breaksep('start')
        exibirmensagem(f'Você morreu.\n\nCausa: {DeathMessage}',False,0,False)
# clear()
# history()