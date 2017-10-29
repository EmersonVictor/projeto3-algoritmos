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
from listaVeiculos import *
from  quicksort import *
import timeit

def testQuicksort():
	#Realiza o teste de tempo de execução das duas implementações do quicksort com o arquivo de veículos e escreve os resultados em um arquivo
	array = createList("../testes/veiculos.txt")
	results = open("qs-results.txt",'a+')
	results.write("---------- TESTE ----------")
	results.write("\n")

	try:
		result = "QS1 = Duração com elementos não ordenados: {0}\n".format(timeQS1(array))
	except RecursionError as e:
		result = "QS1 = Duração com elementos não ordenados: -1\n"

	results.write(result)
	print(result)

	try:
		result = "QS2 = Duração com elementos não ordenados: {0}\n".format(timeQS2(array))
	except RecursionError as e:
		result = "QS2 = Duração com elementos não ordenados: -1\n"

	results.write(result)
	print(result)

	results.write("--\n")


	array = sorted(array, key=lambda x: x.getPlaca())
	try:
		result = "QS1 = Duração com elementos ordenados crescentemente: {0}\n".format(timeQS1(array))
	except RecursionError as e:
		result = "QS1 = Duração com elementos ordenados crescentemente: -1\n"

	results.write(result)
	print(result)

	try:
		result = "QS2 = Duração com elementos ordenados crescentemente: {0}\n".format(timeQS2(array))
	except RecursionError as e:
		result = "QS2 = Duração com elementos ordenados crescentement: -1\n"

	results.write(result)
	print(result)

	results.write("--\n")

	array = sorted(array, key=lambda x: x.getPlaca(),reverse=True)

	try:
		result = "QS1 = Duração com elementos ordenados decrescentemente: {0}\n".format(timeQS1(array))
	except RecursionError as e:
		result = "QS1 = Duração com elementos ordenados decrescentemente: -1\n"

	results.write(result)
	print(result)

	try:
		result = "QS2 = Duração com elementos ordenados decrescentemente: {0}\n".format(timeQS2(array))
	except RecursionError as e:
		result = "QS2 = Duração com elementos ordenados decrescentement: -1\n"

	results.write(result)
	print(result)

	results.write("\n")
	results.close()


def timeQS1(array):
	#Calcula o tempo de execução do 1º algoritmo quicksort
	start = timeit.default_timer()
	quickSort1(array)
	end = timeit.default_timer()
	return (end - start)

def timeQS2(array):
	#Calcula o tempo de execução do 2º algoritmo do quicksort
	start = timeit.default_timer()
	quickSort2(array)
	end = timeit.default_timer()
	return (end - start)

if __name__ == "__main__":
	for x in range(20):
		testQuicksort()
