import json
import os
from funcionario import Funcionario

class LeFuncionario:

    @staticmethod
    def abrir(cpf: str):

        nome_file = cpf + '.json'

        # se encontrar o arquivo
        if (os.path.exists(nome_file)):

            # ler o arquivo e converter para objeto json
            with open(nome_file, 'r') as funcionario_file:
                funcionario_json = json.load(funcionario_file)
            
            # print(funcionario_json)

            funcionario = Funcionario(**funcionario_json)

            print('Dados do Funcionário:')
            print(f'CPF: {funcionario.cpf}')
            print(f'Nome: {funcionario.nome}')
            print(f'Idade: {funcionario.idade}')
            print('Salário: R$ %.2f' % funcionario.salario)
            print(f'Cargo: {funcionario.cargo}')
            habilidades = ', '.join(funcionario.habilidades)
            print(f'Habilidades: {habilidades}')

        else:
            print('Funcinário não encontrado')