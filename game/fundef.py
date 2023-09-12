__ver__='v0.1.0'

from sys import stdout
from time import sleep
import os

def DJpt(DJphrase:str,DJtempo:int,DJespera:int):
    for i in DJphrase:
        stdout.write(i)
        stdout.flush()
        sleep(1/DJtempo)
    sleep(DJespera)

def separacao():
    return'~'*20
sep=separacao()
def separacaoquebra():
    return f'{sep}'
sepbreak=separacaoquebra()

def linebreak(x):
    print('\n'*x)

def sepclear(cltemp: float,clescrevaalgo:int):
    print(sep)
    if clescrevaalgo==0:pass
    elif clescrevaalgo==1:print('Escreva algo!')

    sleep(cltemp)
    os.system('cls')

def clearsep(cltemp:float):
    sleep(cltemp)
    os.system('cls')
    print(sep)

def pergunta(P1,P2,P3):
    print(f'1. {P1}')
    print(f'2. {P2}')
    if P3 is not None:
        print(f'3. {P3}')

def resposta():
    return input('\n-> ')

def movercima(lines=1):
    stdout.write('\x1b[A'*lines)
    stdout.flush()

def primetecla():
    try:
        if os.name == 'nt':
            import msvcrt
            msvcrt.getch()
        else:
            import termios
            termios.tcgetattr(0)
            termios.tcsetattr(0, termios.TCSANOW, termios.tcgetattr(0))
            os.read(0, 1)
    except KeyboardInterrupt:
        pass


def primeclear():
    primetecla()
    clear(0)

def clear(cltemp: float):
    sleep(cltemp)
    os.system('cls')

def creditsIn():
    print(f'{sepbreak}')
    exibirmensagem([f'Programado por:\n\npensativw\n\nAgradecimentos especiais:\n\n3DJhey & Gabriel Morph\n{sepbreak}'],False,0,False)
    primeclear()

def creditsFi():
    exibirmensagem([f'Programado por:\n\npensativw\n\nAgradecimentos especiais:\n\n3DJhey & Gabriel Morph\n{sepbreak}'],False,0,False)
    primeclear()

def confirmmensagem(mensagem,breaklinestart: bool):
    if breaklinestart==True:
        print(sep)
    else:pass
    for mensagem in mensagem:
            print(f'{mensagem}')
            primetecla()
    else:pass

def exibirmensagem(mensagem,breakline:bool,tempo: float,ending:bool):
    if breakline==True:
        print(sep)
    else:pass
    for mensagem in mensagem:
        if ending==True:
            print(f"{mensagem}",end=' ',flush=True)
            sleep(tempo)
        else:
            print(f"{mensagem}",flush=True)
            sleep(tempo)

def thanks():
    print(f'{sep}\nObrigado por jogarem o meu primeiro joguinho! Demorei muito para fazer.\n\nEspero que curtam!\n{sep}')
    primetecla()
    clear(0)
def final():
    confirmmensagem([f'\nESSA FOI A {__ver__}!\n\n{sepbreak}'],True)
    creditsFi()
    print('\nSaindo...')
    sleep(1/2)
    exit()
