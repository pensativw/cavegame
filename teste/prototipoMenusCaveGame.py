import curses
from time import sleep
from typing import List





class Tecla:
    setinha_cima = curses.KEY_UP
    setinha_baixo = curses.KEY_DOWN
    enter = curses.KEY_ENTER



def printMenu(stdscr, selected_row_idx, menu):
    
    stdscr.clear() # limpa tudo
    altura, largura = stdscr.getmaxyx() # pega a altura e largura do console/terminal em pixels
    
    barra = "=" * 25 # TODO fazer esse numero ser a string com maior len da lista
    
    meio = largura//2 - len(barra)//2
    cima = altura//2 - len(menu)
    baixo = altura//2 + len(menu)

    # Barra de Cima
    stdscr.addstr(cima, meio, barra)

    for index, linha in enumerate(menu):
        # dividir por 2 é achar a metado (o meio)
        x = largura//2 - len(linha)//2 
        y = altura//2 - len(menu)//2 + index
        
        

        if index == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, linha)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, linha)

    # Barra de Baixo
    stdscr.addstr(baixo, meio, barra)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()
    x = largura//2 - len(text)//2
    y = altura//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def print_center_border(stdscr, text, limpar=False):
    if limpar:
        stdscr.clear()
    altura, largura = stdscr.getmaxyx()
    y = altura//2 
    stdscr.addstr(y, 0, text)
    stdscr.refresh()



def mensagem(stdscr, texto, tempo=3, pause=True, limpar=True):
    """
    Mostra uma determinada mensagem em um intervalo de tempo especificado.
    O tempo é calculado dividindo o comprimento do tempo pelo tempo 
    obtendo assim o numero que deve ser posto no sleep (geralmente
    esse número é um float muito pequeno)

    Caso a função receba pause = True, ela ira pausar e printar a mensagem
    de "Pressione Enter para continuar", caso continuar ira pular 
    para a proxima tela de dialogo ou texto.

    A função usa o print_center_border para escrever o texto no meio da altura
    da tela e um pouco afastado do canto esquerdo.

    Limpar é se caso o console/terminal precise ser limpo e vir novos textos.
    """
    intervalo_tempo = tempo / len(texto)

    for i,v in enumerate(texto):
        txt: str = texto[0:i+1]
        print_center_border(stdscr, f"{txt}", limpar)
        sleep(intervalo_tempo)

    if pause: 
        t = " " * 4
        n = txt.count("\n") + 3
        altura, largura = stdscr.getmaxyx()
        y = altura//2 + n
        stdscr.addstr(y, 0, f"{t}Pressione Enter para continuar...") # é como o print (adiciona texto na tela)
        stdscr.getch() # Espera o Input do Usuário



def MostrarOpcoes(stdscr, menu: List[str]) -> None:

    # Configuração inicial de cores para mostrar as opções de um menu iterativo
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) 
    
    linha_atual = 0

    # Printar primeiro para depois mover
    printMenu(stdscr, linha_atual, menu)

    while True:
        tecla = stdscr.getch()

        if tecla == Tecla.setinha_cima and linha_atual > 0:
            linha_atual -= 1 # Move pra cima

        elif tecla == Tecla.setinha_baixo and linha_atual < len(menu)-1:
            linha_atual += 1 # Move para baixo

        elif tecla == Tecla.enter or tecla in [10, 13]:
            # 'linha_atual' é o index na lista
            # 'menu[linha_atual]' é o texto literal que está na lista
            stdscr.clear()
            return menu[linha_atual]
        
        # Printar Menu Atualizado ao fim
        printMenu(stdscr, linha_atual, menu)


def MostrarMenu(stdscr, menu: List[str]) -> None:
    """Responsavel por Mostrar o Menu inicial do Jogo."""
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    linha_atual = 0
    # Printar primeiro para depois mover
    printMenu(stdscr, linha_atual, menu)

    while True:
        tecla = stdscr.getch()

        if tecla == Tecla.setinha_cima and linha_atual > 0:
            linha_atual -= 1 # Move pra cima

        elif tecla == Tecla.setinha_baixo and linha_atual < len(menu)-1:
            linha_atual += 1 # Move para baixo

        elif tecla == Tecla.enter or tecla in [10, 13]:
            # Ação apos apertar Enter
            if linha_atual == 0:
                stdscr.clear()
                linhaPrincipal(stdscr) # Rota principal da Historia 
                stdscr.getch() 
            elif linha_atual == 1:
                ... # TODO implementar 
                # stdscr.getch()
            elif linha_atual == 2:
                ... # TODO implementar 
                # stdscr.getch()
            elif linha_atual == 3:
                ... # TODO implementar 
                # stdscr.getch()
            elif linha_atual == 4:
                
                mensagem(stdscr,"\tVocê está prestas a Sair do Jogo!", 0.2)
                stdscr.getch()
                break




            if linha_atual == len(menu)-1: # Sair do programa caso seja a ultima linha
                break

        
        # Printar Menu Atualizado ao fim
        printMenu(stdscr, linha_atual, menu)
    
    return linha_atual


def linhaPrincipal(stdscr):
    # Espaçamentos
    t = " " * 8
    t1 = " " * 15
    t2 = " " * 5

    mensagem(stdscr, f"{t}Você acabou de acordar....{t1}\n{t}Tu mal consegue enxergar...{t2}\n{t}O que você faz?\n", 9, limpar=False)

    opcao = MostrarOpcoes( stdscr,
        [    
            "Gritar Socorro!",
            "Se levantar e procurar a saída!",
            "Nada...",
        ]
    )

    if opcao == "Gritar Socorro!":
        mensagem(stdscr, f"{t}Você Grita um Pedra Cai em Você. Você Morre!", 3)
        
    if opcao == "Se levantar e procurar a saída!":
        mensagem(stdscr, f"{t}Você Corre Tropeça numa pedra Bate de Cabeça na Pedra. Você Morre!", 3)
        
    if opcao == "Nada...":
        mensagem(stdscr, f"{t}Você não fez nada... Você Morre!", 3)
        

    mensagem(stdscr, f"{t}Fim! Obrigado Por Jogar", 3)



def iniciarJogo(stdscr):
    curses.curs_set(0) # Remove o cursor piscando na Tela

    # Inicio do Game

    MostrarMenu(
        stdscr, 
        [    
            "Cave the Game",
            "Instruções",
            "Agradecimentos",
            "Créditos",
            "Sair",
        ]
    )









def main():
    curses.wrapper(iniciarJogo)



if __name__ == "__main__":
    # Execução da Função Principal
    main()
