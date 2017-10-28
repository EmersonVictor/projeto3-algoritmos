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

	results.write("Teste")
	results.write("")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))
		result = "Duração com {0} elementos não ordenados: qs1 {1} || qs2 {2}".format(size, timeQS1(array), timeQS1(array))
		results.write(result)
		print(result)

	results.write("--")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))
		array = sorted(array)
		result = "Duração com {0} elementos ordenados crescentemente: qs1 {1} || qs2 {2}".format(size, timeQS1(array), timeQS1(array))
		results.write(result)
		print(result)

	results.write("--")

	for size in sizes:
		array = list(numpy.random.randint(1000,size=size))
		array = sorted(array, reverse=True)
		result = "Duração com {0} elementos ordenados decrescentemente: qs1 {1} || qs2 {2}".format(size, timeQS1(array), timeQS1(array))
		results.write(result)
		print(result)

	results.write("")
	results.close()

def timeQS1(array):
	start = time.default_timer()
	quickSort1(array)
	end = time.default_timer()
	return (end - start)

def timeQS2(array):
	start = time.default_timer()
	quickSort2(array)
	end = time.default_timer()
	return (end - start)
