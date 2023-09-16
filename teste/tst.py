import curses
from rich.text import Text

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Esconde o cursor do terminal
    stdscr.clear()
    
    text = Text("Texto centralizado com Rich!")
    text.stylize("bold underline")
    
    # Converte o objeto Text para uma string formatada
    formatted_text = text.__str__()

    print_center(stdscr, formatted_text)

    stdscr.getch()  # Aguarda uma entrada do usuário

curses.wrapper(main)  # Chama a função principal e lida com inicialização e encerramento do curses
