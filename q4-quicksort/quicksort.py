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


def quickSort1(array):
	# Ordenação quicksort com implementação utilizando método quebra e concatenação de lista
	if array == []:
		return []
	else:
		pivot = array.pop(0)
		return quickSort1([x for x in array if x.getPlaca() < pivot.getPlaca()]) + [pivot] + quickSort1([x for x in array if x.getPlaca() >= pivot.getPlaca()])

def quickSort2(array):
	# Ordenação quicksort com implementação utilizando método de partição
	qs2(array, 0, len(array) - 1)
	return array

def qs2(array, left, right):
	# Ordenação quicksort com implementação utilizando método de partição - função auxiliar
	if left >= right:
		return
	else:
		pivot = partition(array, left, right)
		qs2(array, left, pivot - 1)
		qs2(array, pivot + 1, right)

def partition(array, left, right):
	# Divisão do array em duas partes, menores que o pivô e maiores que o pivô
	pivot = array[left]
	cont = True
	l = left
	r = right + 1

	while cont:
		l += 1
		while array[l].getPlaca() < pivot.getPlaca():
			if l >= right:
				break
			l += 1

		r -= 1
		while array[r].getPlaca() > pivot.getPlaca():
			if r <= left:
				break
			r -= 1

		if l >= r:
			cont = False
		else:
			array[l], array[r] = array[r], array[l]

	array[left], array[r] = array[r], array[left]
	return r
