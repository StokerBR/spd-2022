from typing import List

class Funcionario:

    def __init__(self, cpf: str, nome: str, idade: int, salario: float, cargo: str, habilidades: List[str]):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo
        self.habilidades = habilidades