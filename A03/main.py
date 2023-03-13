from salva_funcionario import SalvaFuncionario
from le_funcionario import LeFuncionario

user_input = input('Deseja salvar(s) ou ler(l) um funcionário? (s/l)\n')

if (user_input == 's'):
    SalvaFuncionario.ler()

elif (user_input == 'l'):
    cpf = input('CPF do funcionário: ')
    LeFuncionario.abrir(cpf)
