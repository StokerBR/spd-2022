from enum import Enum
 
class Periodicidade(Enum):
    DIA = 1
    SEMANA = 2
    MES = 3
    ANO = 4
 
class Situacao(Enum):
    AGENDADO = 1
    CANCELADO = 2
    REALIZADO = 3