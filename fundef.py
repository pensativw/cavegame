import time,sys

def DJpt(DJphrase,DJtempo):
    for i in DJphrase:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1/DJtempo)


def TUTO():
    INS=input('\nAntes de tudo, deseja ver instruções para saber o que vai fazer? -> ').lower()
    INS_Open=False
    while True:
        if INS in ['sim','s','y','yes']:
            input('\nO jogo é de escolhas, se você fez algo, no futuro tu pode morrer.')
            input('\nHá caminhos secretos nesse jogo, tipo a primeira escolha.')
            input('\nPorém, não vão ser todas as escolhas que irão ter opções secretas.')
            input('\nEspero que se diverta!')
            INS_Open=True
        elif INS in ['n','não','nao','no']:
            INS_Open=True
            break
        elif INS in ['']:
            INS=input('\nEnter mais uma vez para não ir pro tutorial. -> ')
            if INS == '':INS_Open=True
            break
        else:
            INS=input('Sim ou não -> ')
            continue
            
        if INS_Open==True:break
    