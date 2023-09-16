__ver__='v0.1.5'

from sys import stdout
from time import sleep
import os

def DJpt(DJphrase:str,DJtempo:int,DJespera:int,persona=''):
    for i in DJphrase:
        stdout.write(i)
        stdout.flush()
        sleep(1/DJtempo)
    if persona=='':
        pass
    else:
        sleep(1/2)
        print(' ~ ',end='')
        sleep(1/DJtempo)
        for ie in persona:
            
            stdout.write(ie)
            stdout.flush()
            sleep(1/DJtempo)
    sleep(DJespera)

def sep(quebras=0):
    separacao='~'*40
    if quebras >=1:
        print('\n' * quebras)
    return separacao

def breaksep(sepa='end' ,limpartela=0,temp=0):
    if sepa=='padrao':   # é o padrão pra avançar
        print(sep())
        clear(1/4)
    elif sepa=='end': # primeiro a separação, depois limpar o histórico
        print(sep())
        if limpartela==1:clear(temp)
    elif sepa=='start': # primeiro a limpeza do histórico, depois a separação
        if limpartela==1:clear(temp)
        print(sep())

def pergunta(P1,P2,P3):
    print(f'1. {P1}')
    print(f'2. {P2}')
    if P3 is not None:
        print(f'3. {P3}')

def resposta():
    return input('\n-> ')

# def movercima(lines=1):
#     stdout.write('\x1b[A'*lines)
#     stdout.flush()

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

def breakline(int:int):
    return print('\n')

def primeclear():
    primetecla()
    clear(0)

def clear(cltemp: float=0):
    sleep(cltemp)
    os.system('cls')

def creditsIn():
    print(sep())
    print(__ver__)
    exibirmensagem([f'\nProgramado por:\n\npensativw\n\nAgradecimentos especiais:\n\n3DJhey & Gabriel Morph\n{sep()}'],False,0,False)
    primeclear()

def creditsFi():
    exibirmensagem([f'Programado por:\n\npensativw\n\nAgradecimentos especiais:\n\n3DJhey & Gabriel Morph\n{sep()}'],False,0,False)
    primeclear()

def confirmmensagem(mensagem,seplinestart: bool):
    if seplinestart==True:
        print(sep())
    if isinstance(mensagem,str):
        print(mensagem)
        stdout.flush()
        primetecla()
    elif isinstance(mensagem,list):
        for msg in mensagem:
            print(msg)
            stdout.flush()
            primetecla()

def exibirmensagem(mensagem,breakline:bool,tempo: float,ending:bool):
    if breakline==True:
        sep()
    if isinstance(mensagem,str):
        print(mensagem)
    if isinstance(mensagem,list):
        for mensagem in mensagem:
            if ending==True:
                print(f"{mensagem}",end=' ',flush=True)
                sleep(tempo)
            else:
                print(f"{mensagem}",flush=True)
                sleep(tempo)

def thanks():
    print(f'{sep()}\nObrigado por jogarem o meu primeiro joguinho! Demorei muito para fazer.\n\nEspero que curtam!\n{sep()}')
    primetecla()
    clear(0)
def final():
    confirmmensagem([f'\nESSA FOI A {__ver__}!\n\n{sep()}'],True)
    creditsFi()
    print('\nSaindo...')
    sleep(1/2)
    exit()
