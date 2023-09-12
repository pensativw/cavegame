
from time import sleep
from fundef import *
 
sep=separacao()


# from main import player_name

# def decorator_com_linha(func):
#     def funcao_auxiliar(*args, **kwargs):
#         print("=" * 20)  # Linha no início da função
#         result = func(*args, **kwargs)
#         print("=" * 20)  # Linha no final da função
#         return result
#     return funcao_auxiliar
# @decorator_com_linha

def mainmenu():
    while True:
        start=input(f'{sep}\nE. Cave the Game\nI. Instruções\nA. Agradecimentos\nC. Créditos\nQ. Sair\n\n-> ').lower()
        if start=='q':
            print('\nSaindo...')
            sleep(1/2)
            exit()
        elif start=='e':
            sepclear(1/4,False)
            break
        elif start=='c':
            sepclear(1/4,0)
            creditsIn()
        elif start=='i':
            sepclear(1/4,0)
            tuto()
        elif start=='a':
            sepclear(1/4,0)
            thanks()
        else:
            clear(0)
            continue


def getName(texto: str, erro: str) -> str:
    while True:
        getname = input(texto)
        if getname.isalpha() and len(getname) > 3:
            name_ye = input(f'\n{getname}... Tem certeza? -> ').lower()
            if name_ye in ['sim', 's', 'y', 'yes', 'tenho']:
                print(f'\nOk, meu nome é {getname}!\n{sep}')
                clear(0.5)
                return getname
            else:
                sepclear(1/4,1)
                continue
        else:
            print(f'\n{erro}\n{sep}')
            primeclear()

def getPlayerName() -> str:
    name = getName(texto=f'{sep}\nEscreva seu nome -> ',
    erro=f'O nome deve conter apenas letras e ter mais de 3 caracteres')
    return name

# def tuto():
#     print(f'{sep}\nAntes de começar, deseja ver as instruções para saber o que esperar?\n')
#     while True:
#         resposta01 = input(f'S/N/Enter -> ').lower()

#         if resposta01 == '':
#             confirmacao = input(f'\nTem certeza que NÃO quer ver o tutorial? -> ').lower()
#             if confirmacao in ['sim', 's', 'y', 'yes']:
#                 resposta01='n'
#                 continue
#             elif confirmacao in['nao','não','no','n']:
#                 resposta01='s'
#                 continue
#             elif confirmacao=='':
#                 resposta01='n'
#         if resposta01 in ['sim', 's', 'y', 'yes']:
#             clearsep(1/4)
#             mensagem = [
#                 'O jogo é baseado em escolhas, e suas decisões afetarão o rumo da história.',
#                 'Tem algumas escolhas que você tem que chutar qual é o número fora da lista, pode ser uma referência à algo, por exemplo.',
#                 'Há caminhos secretos neste jogo, tipo a primeira escolha que você vai fazer.',
#                 'As animações de texto são usadas para representar um personagem falando.',
#                 'Texto estático é narrativa.',
#                 'Lembre-se de que nem todas as escolhas têm opções secretas.',
#                 'Espero que se divirta jogando!'
#             ]
#             print(sep)
#             exibir_mensagem(mensagem)
#             clearsep(1/4)
#             break
#         elif resposta01 in ['nao','n','não','no']:
#             clearsep(1/4)
#             break
#         else:
#             print(f'\nEscreva o que está pedindo.\n{sep}')
#             clear(3)
#             print(f'{sep}\nAntes de começar, deseja ver as instruções para saber o que esperar?\n')
def tuto():
    print(sep)
    mensagem = [
        'O jogo é baseado em escolhas, e suas decisões afetarão o rumo da história.\n',
        'Tem algumas escolhas que você tem que chutar qual é o número fora da lista, pode ser uma referência à algo, por exemplo.\n',
        'Há caminhos secretos neste jogo, tipo a primeira escolha que você vai fazer.\n',
        'As animações de texto são usadas para representar um personagem falando.\n',
        'Texto estático é narrativa.\n',
        'Lembre-se de que nem todas as escolhas têm opções secretas.\n'
    ]
    confirmmensagem(mensagem,False)
    print(f'Espero que se divirta jogando!\n{sep}')
    primeclear()
