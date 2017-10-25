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
    #Ordenação quicksort com implementação utilizando método quebra e concatenação de lista
    if array == []:
        return []
    else:
        pivot = array.pop(0)
        return quickSort1([num for num in array if num < pivot ]) + [pivot] + quickSort1([num for num in array if num >= pivot])

def quickSort2(array):
    #Ordenação quicksort com implementação utilizando método de partição
    qs2(array,0, len(array)-1)
    return array

def qs2(array, left, right):
    #Ordenação quicksort com implementação utilizando método de partição - função auxiliar
    if left >= right:
        return
    else:
        pivot = partition(array,left,right)
        qs2(array,left,pivot-1)
        qs2(array,pivot+1,right)


def partition(array, left, right):
    #Divisão do array em duas partes, menores que o pivô e maiores que o pivô
    pivot = array[left]
    cont = True
    l = left + 1
    r = right

    while cont:
        while array[l] < pivot:
            if l >= right:
                break
            l += 1

        while array[r] > pivot:
            if r <= left:
                break
            r -= 1

        if l >= r:
            cont = False
        else:
            array[l], array[r] = array[r], array[l]

    array[left], array[r] = array[r], array[left]
    return r
