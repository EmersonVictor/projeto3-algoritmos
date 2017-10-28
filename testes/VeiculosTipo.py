 # -*- coding: utf-8 -*-
import sys
sys.path.append('../testes')
from  VeiculoAbstrato import Veiculo

'''
Descrição: Classe que guarda os objetos do tipo Carro e é uma classe derivada da Super Classe Veiculo (Classe abstrata)

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
    Ela recebe todos os parâmetros que veículo recebe, mais a quantidade de portas que possui, podendo ser 2 ou 4.
'''
class Carro(Veiculo):
    def __init__(self, fabricante, modelo, quantidadePortas, autonomia, ano, placa, renavam, chassi, reservado = False):
        Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado)
        self.__quantidadePortas = self.__validaQuantPortas(quantidadePortas)

    def __repr__(self):
        return "carro\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(self.getFabricante(), self.getModelo(), self.getAno(), self.__quantidadePortas, self.getAutonomia(), self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())

    # Descrição: O método realiza a validação da quantidade de portas, analisando se possui 2 ou 4, se não aciona um erro
    def __validaQuantPortas(self, quantidadePortas):
        if int(quantidadePortas) != 2 and int(quantidadePortas) != 4:
            raise ValueError("Quantidade inválida, o carro deve possuir 2 ou 4 portas")
        return int(quantidadePortas)

'''
Descrição: Classe que guarda os objetos do tipo Van e é uma classe derivada da Super Classe Veiculo (Classe abstrata)

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
    Ela recebe todos os parâmetros que veículo recebe, mais a capacidade de pessoas.
'''
class Van(Veiculo):
    def __init__(self, fabricante, modelo, capacidadePessoas, autonomia, ano, placa, renavam, chassi, reservado = False):
        Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado)
        self.__capacidadePessoas = self.__validaCapacidadePessoas(capacidadePessoas)

    def __repr__(self):
        return "van\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(self.getFabricante(), self.getModelo(), self.getAno(), self.__capacidadePessoas, self.getAutonomia(), self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())

    #Descrição: realiza a validação da capacidade de pessoas, analisando se é um número
    def __validaCapacidadePessoas(self, capacidade):
        if capacidade.isdigit():
            return int(capacidade)
        raise ValueError("A capacidade de pessoas deve ser um número")

'''
Descrição: Classe que guarda os objetos do tipo Utilitario e é uma classe derivada da
           Super Classe Veiculo (Classe abstrata)

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
    Ela recebe todos os parâmetros que veículo recebe, mais a capacidade da Caçamba
'''
class Utilitario(Veiculo):
    def __init__(self, fabricante, modelo, capacidadeCacamba, autonomia, ano, placa, renavam, chassi, reservado = False):
        Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado)
        self.__capacidadeCacamba = self.__validaCapacidadeCacamba(capacidadeCacamba)

    def __repr__(self):
        return "ute\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(self.getFabricante(), self.getModelo(), self.getAno(),self.__capacidadeCacamba, self.getAutonomia(), self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())

    #Descrição: realiza a validação da capacidade da Caçamba, analisando se é um número
    def __validaCapacidadeCacamba(self, capacidade):
        if capacidade.isdigit():
            return int(capacidade)
        raise ValueError("Capacidade da caçamba deve ser um número")
