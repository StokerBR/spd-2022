import xmltodict
import os
from funcionario import Funcionario

class LeFuncionario:

    @staticmethod
    def abrir(cpf: str):

        nome_file = cpf + '.xml'

        # se encontrar o arquivo
        if (os.path.exists(nome_file)):

            # ler o arquivo e converter para objeto xml
            with open(nome_file, 'r') as funcionario_file:
                funcionario_xml = xmltodict.parse(funcionario_file.read())

            print(funcionario_xml)
            
            funcionario = Funcionario(**funcionario_xml['funcionario'])

            print('Dados do Funcionário:')
            print(f'CPF: {funcionario.cpf}')
            print(f'Nome: {funcionario.nome}')
            print(f'Idade: {funcionario.idade}')
            print('Salário: R$ %.2f' % float(funcionario.salario))
            print(f'Cargo: {funcionario.cargo}')
            habilidades = ', '.join(funcionario.habilidades)
            print(f'Habilidades: {habilidades}')

        else:
            print('Funcinário não encontrado')