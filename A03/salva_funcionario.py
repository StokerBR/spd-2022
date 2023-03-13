import xmltodict
import re
from funcionario import Funcionario

class SalvaFuncionario:

    @staticmethod
    def ler():

        print('Insira os dados do Funcionário')

        cpf = input('CPF: ')
        cpf = re.sub('[^0-9.-]', '', cpf)

        nome = input('Nome: ')
        idade = int(input('Idade: '))
        salario = float(input('Salário: ').replace(',','.'))
        cargo = input('Cargo: ')

        habilidades = input('Habilidades (separadas por vírgula): ')
        habilidades = habilidades.split(',')
        habilidades = list(map(str.strip, habilidades)) # dar 'trim' em todas as habilidades

        funcionario = Funcionario(cpf, nome, idade, salario, cargo, habilidades)

        SalvaFuncionario.salvar(funcionario)

    @staticmethod
    def salvar(funcionario: Funcionario):

        # dicionario do funcionario
        funcionario_dict = {
            'funcionario': {
                'cpf': funcionario.cpf,
                'nome': funcionario.nome,
                'idade': funcionario.idade,
                'salario': funcionario.salario,
                'cargo': funcionario.cargo,
                'habilidades': funcionario.habilidades,
            }
        }
        
        # salvar funcionario em xml
        with open(f'{funcionario.cpf}.xml', 'w') as funcionario_file:
            funcionario_file.write(xmltodict.unparse(funcionario_dict))