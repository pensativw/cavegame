
from time import sleep
from fundef import *

def mainmenu():
    while True:
        start=input(f'{sep()}\nE. Cave the Game\nI. Instruções\nA. Agradecimentos\nC. Créditos\nQ. Sair\n\n-> ').lower()
        if start=='q':
            print('\nSaindo...')
            sleep(1/2)
            exit()
        elif start=='e':
            breaksep('end',1,1/4)
            break
        elif start=='c':
            breaksep('end',1,1/4)
            creditsIn()
        elif start=='i':
            breaksep('end',1,1/4)
            tuto()
        elif start=='a':
            breaksep('end',1,1/4)
            thanks()
        else:
            clear(0)
            continue


def getName(texto: str, erro: str) -> str:
    while True:
        getname = input(texto)
        if getname.isalpha() and len(getname) > 3:
            name_ye = input(f'\n{getname[0].upper() + getname[1:]}... Tem certeza? -> ').lower()
            if name_ye in ['sim', 's', 'y', 'yes', 'tenho']:
                breaksep('padrao')
                name = getname[0].upper() + getname[1:]
                return name
            else:
                breaksep('padrao')
                continue
        else:
            print(f'\n{erro}\n{sep()}')
            primeclear()


def getPlayerName() -> str:
    name = getName(texto=f'{sep()}\nEscreva seu nome -> ',
    erro=f'O nome deve conter apenas letras e ter mais de 3 caracteres')
    return name

def getFriend00() -> str:
    name = getName(texto=f'{sep()}\nEscreva o nome dele -> ',
    erro=f'O nome deve conter apenas letras e ter mais de 3 caracteres')
    return name

def tuto():
    print(sep())
    mensagem = [
        'O jogo é baseado em escolhas, e suas decisões afetarão o rumo da história.\n',
        'Tem algumas escolhas que você tem que chutar qual é o número fora da lista, pode ser uma referência à algo, por exemplo.\n',
        'Há caminhos secretos neste jogo, tipo a primeira escolha que você vai fazer.\n',
        'As animações de texto são usadas para representar um personagem falando.\n',
        'Texto estático é narrativa.\n',
        'Lembre-se de que nem todas as escolhas têm opções secretas.\n'
    ]
    confirmmensagem(mensagem,False)
    print(f'Espero que se divirta jogando!\n{sep()}')
    primeclear()
