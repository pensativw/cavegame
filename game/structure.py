from fundef import creditsIn,__ver__,DJpt, exibir_mensagem, separacao
import sys,time
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

def starting():
    while True:
        start=input(f'{sep}\nE. Cave the Game\nC. Créditos\nQ. Sair\n\n-> ').lower()
        if start=='q':
            print('Saindo...')
            time.sleep(1/4)
            sys.exit()
        elif start=='e':
            break
        elif start=='c':
            creditsIn()
        else: continue
        
def getName(texto: str, erro: str) -> str:
    while True:
        getname = input(texto)
        if getname.isalpha() and len(getname) > 3:
            name_ye = input(f'\n{getname}... Tem certeza? -> ').lower()
            if name_ye in ['sim', 's', 'y', 'yes']:
                print(f'\nOk, meu nome é {getname}!\n{sep}')
                return getname
        else:
            print(erro)



def getPlayerName() -> str:
    name = getName(texto=f'{sep}\nEscreva seu nome -> ',
    erro=f'O nome deve conter apenas letras e ter mais de 3 caracteres')
    return name





def tuto():
    print(f'{sep}\nAntes de começar, deseja ver as instruções para saber o que esperar?\n')
    resposta00 = True

    while True:
        resposta01 = input(f'Sim, não ou Enter -> ').lower()

        if resposta01 == '':
            confirmacao = input(f'\nTem certeza que NÃO quer ver o tutorial? -> ').lower()
          
            if confirmacao in ['sim', 's', 'y', 'yes','']:
                break
            elif confirmacao in ['nao','n','não','no']:
                resposta01 = 'sim'
            else:continue
        if resposta01 in ['sim', 's', 'y', 'yes']:
            print(f'{sep}')
            mensagem = [
                'O jogo é baseado em escolhas, e suas decisões afetarão o rumo da história.',
                'Tem algumas escolhas que você tem que chutar qual é o número, pode ser uma referência à algo, por exemplo.',
                'Há caminhos secretos neste jogo, tipo a primeira escolha que você vai fazer.',
                'As animações de texto são usadas para representar um personagem falando.',
                'Texto estático é narrativa.',
                'Lembre-se de que nem todas as escolhas têm opções secretas.',
                'Espero que se divirta jogando!'
            ]
            exibir_mensagem(mensagem)
            break
        elif resposta01 in ['nao','n','não','no']:
            break
        else:
            input(f'{sep}\nEscreva o que está pedindo.')
            input(f'{sep}\nEscreva o que está pedindo.')
