__ver__='0.0.31a'
import time,sys
def DJpt(DJphrase:str,DJtempo:int):
    for i in DJphrase:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1/DJtempo)

def separacao():
    return'~'*10

sep=separacao()

def creditsIn():
    input(f'{sep}\nVersão {__ver__}')
    input('\nProgramado por:\npensativw')
    input('\nRedes sociais:\nPraticamente tudo é pensativw')
    input(f'\nAgradecimentos especiais:\n3DJhey\nGabriel Morph')
    
def creditsFi():
    input(f'{sep}\nVersão {__ver__}')
    input('\nProgramado por:\npensativw')
    input('\nRedes sociais:\nPraticamente tudo é pensativw')
    input(f'\nAgradecimentos especiais:\n3DJhey\nGabriel Morph\n{sep}\n')

def final():
    input(f'\nESSA FOI A ALPHA!\n')
    
    creditsFi()
def exibir_mensagem(mensagem):
    for mensagem in mensagem:
        input(mensagem)
