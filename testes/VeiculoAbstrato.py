 # -*- coding: utf-8 -*-

'''
Descrição: A classe Veiculo é uma classe abstrata que funciona para construir os tipos de veículo

Utilização: A Classe realiza validações dos valores padrões

Parâmetros:
    Fabricante: String que representa o fabricante do veículo
    Modelo: string representando o modelo do veículo
    Autonomia: Número inteiro medido em Km/L
    Ano: Interiro formado por 4 digitos
    Placa: 3 letras seguidas de 4 números (ex: KKK0000)
    Renavam: 9 dígitos inteiros
    Chassi: Mistura de letras e números seguindo o formato 3TT333TT33T333333 (3 = Números/ T = Letras)
    Reservado: Recebe True, para não reservado, ou False, para reservado
'''
import sys
sys.path.append('..')

class Veiculo:
    def __init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__autonomia = autonomia
        self.__ano = self.__validaAno(ano)
        self.__placa = self.__validaPlaca(placa)
        self.__renavam = self.__validaRenavam(renavam)
        self.__chassi = chassi
        self.__reservado = self.__validaReservado(reservado)


    # Descrição: O método __validaPlaca realiza a validação da placa, analisando se o string está no formato correto
    def __validaPlaca(self, placa):
        if not (placa[0:3].isdigit()) and placa[4:7].isdigit() and len(placa) == 8:
            return placa
        raise ValueError("Placa {0} não segue o formato correto".format(placa))

    # Descrição: O método __validaRenavam realiza a validação do RENAVAM, analisando se todos os digitos do string são números e se possui o tamanho correto
    def __validaRenavam(self, renavam):
        if renavam.isdigit() and len(str(renavam)) == 11:
            return int(renavam)
        raise ValueError("Renavam {0} não segue o formato".format(renavam))

    # Descrição: O método __validaReservado realiza a validação do valor recebido em reservado, analisando se é um valor booleano
    def __validaReservado(self, reservado):
        if isinstance(reservado, bool):
            return reservado
        elif reservado.lower() == "true":
                        return True
        elif reservado.lower() == "false":
                        return False
        raise TypeError("Reservado aceita apenas os valores True ou False")

    # Descrição: O método __validaAno realiza a validação do ano recebido, analisando se é um inteiro formado por 4 digitos
    def __validaAno(self, ano):
        if ano.isdigit() and len(str(ano)) == 4:
            return int(ano)
        raise ValueError("{0} não segue o formato de ano correto".format(ano))

    # Descrição: O método realiza a troca do valor booleano presente na variável reservado
    def mudaReserva(self):
        if self.__reservado == True:
            self.__reservado = False
        else:
            self.__reservado = True

    # Descrição: Obtém atributo fabricante
    def getFabricante(self):
        return self.__fabricante

    # Descrição: Obtém atributo modelo
    def getModelo(self):
        return self.__modelo

    # Descrição: Obtém atributo autonomia
    def getAutonomia(self):
        return self.__autonomia

    # Descrição: Obtém atributo ano
    def getAno(self):
        return self.__ano

    # Descrição: Obtém atributo placa
    def getPlaca(self):
        return self.__placa

    # Descrição: Obtém atributo chassi
    def getChassi(self):
        return self.__chassi

    # Descrição: Obtém atributo renavam
    def getRenavam(self):
        return self.__renavam

    # Descrição: Obtém atributo reservado
    def getReservado(self):
        return self.__reservado
