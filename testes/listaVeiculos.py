# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados

Autor:	Emerson Victor Ferreira da Luz (evfl)
Email:	evfl@cin.ufpe.br
Data:	2017-10-22

Copyright(c) 2017 Emerson Victor
'''
import sys
sys.path.append('../testes')
from VeiculosTipo import *

def createList(path):
    array = []
    vehiclesFiles = open(path, "r")
    vehiclesFiles.readline()

    for vehicle in vehiclesFiles:
            auxVehicle = vehicle.split()
            array.append(newVehicle(auxVehicle[0], auxVehicle[1], auxVehicle[2], auxVehicle[3], auxVehicle[4], auxVehicle[5], auxVehicle[6], auxVehicle[7], auxVehicle[8], auxVehicle[9]))

    vehiclesFiles.close()

    return array

def newVehicle(tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado = False ):
	if tipo.lower() == "carro":
		return Carro(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado)
	elif tipo.lower() == "van":
		return Van(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado)
	elif tipo.lower() == "ute":
		return Utilitario(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado)
	else:
		raise ValueError("Não existe veículo do tipo {0}".format(tipo))
