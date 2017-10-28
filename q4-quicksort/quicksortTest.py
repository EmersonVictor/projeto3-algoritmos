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
from quicksort import *
import numpy
import timeit

def testQuicksort():
	sizes = [50, 100, 500, 1000, 5000, 10000]
	results = open("qs-results.txt",'a+')

	results.write("---------- TESTE ----------")
	results.write("\n")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))

		try:
			result = "QS1 = Duração com {0} elementos não ordenados: {1}\n".format(size, timeQS1(array))
		except RecursionError as e:
			result = "QS1 = Duração com {0} elementos não ordenados: -1\n".format(size)

		results.write(result)
		print(result)

		try:
			result = "QS2 = Duração com {0} elementos não ordenados: {1}\n".format(size, timeQS2(array))
		except RecursionError as e:
			result = "QS2 = Duração com {0} elementos não ordenados: -1\n".format(size)

		results.write(result)
		print(result)

	results.write("--\n")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))
		array = sorted(array)

		try:
			result = "QS1 = Duração com {0} elementos ordenados crescentemente: {1}\n".format(size, timeQS1(array))
		except RecursionError as e:
			result = "QS1 = Duração com {0} elementos ordenados crescentemente: -1\n".format(size)

		results.write(result)
		print(result)

		try:
			result = "QS2 = Duração com {0} elementos ordenados crescentemente: {1}\n".format(size, timeQS2(array))
		except RecursionError as e:
			result = "QS2 = Duração com {0} elementos ordenados crescentement: -1\n".format(size)

		results.write(result)
		print(result)

	results.write("--\n")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))
		array = sorted(array, reverse=True)

		try:
			result = "QS1 = Duração com {0} elementos ordenados crescentemente: {1}\n".format(size, timeQS1(array))
		except RecursionError as e:
			result = "QS1 = Duração com {0} elementos ordenados crescentemente: -1\n".format(size)

		results.write(result)
		print(result)

		try:
			result = "QS2 = Duração com {0} elementos ordenados decrescentemente: {1}\n".format(size, timeQS2(array))
		except RecursionError as e:
			result = "QS2 = Duração com {0} elementos ordenados decrescentement: -1\n".format(size)

		results.write(result)
		print(result)

	results.write("\n")
	results.close()

def timeQS1(array):
	start = timeit.default_timer()
	quickSort1(array)
	end = timeit.default_timer()
	return (end - start)

def timeQS2(array):
	start = timeit.default_timer()
	quickSort2(array)
	end = timeit.default_timer()
	return (end - start)

if __name__ == "__main__":
	testQuicksort()
