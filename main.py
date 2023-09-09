
from fundef import final, separacao,separacao
from history import History
from structure import getPlayerName, starting, tuto

sep=separacao()

##  Estou aprendendo a usar o Python criando esse jogo em linha de comando.
##  Críticas construtivas são aceitas.

print(sep)
input('Essa versão do jogo está imcompleta. Se você gostar eu agradeço.')

starting()
tuto()
player_name=getPlayerName()
History.history()
final()