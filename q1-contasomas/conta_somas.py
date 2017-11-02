# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados

Autor:  Emerson Victor Ferreira da Luz (evfl)
Email:  evfl@cin.ufpe.br
Data:   2017-10-22

Copyright(c) 2017 Emerson Victor
'''

def countSums(array):
    #Conta a quantidade de triplas que somadas resultam em zero
    mergeSort(array)
    size = len(array)
    total = 0

    for i in range(size):
        for j in range(i+1, size):
            if binarySearch(-array[i]-array[j], array) > j:
                total += 1

    return total

def binarySearch(number, array):
    #Realiza uma bunca binária em um vetor, retornando a posição caso encontre ou -1 caso não encontre
    start = 0
    end = len(array) - 1

    while start <= end:
        position = (start + end) // 2
        if array[position] > number:
            end = position - 1
        elif array[position] < number:
            start = position + 1
        else:
            return position

    return -1


def mergeSort(array):
    # Ordenação por meio do merge sort
    global aux
    aux = list(array)
    mergeSortAux(array, 0, len(array) - 1)
    del aux


def mergeSortAux(array, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    mergeSortAux(array, left, middle)
    mergeSortAux(array, middle + 1, right)
    merge(array, left, middle, right)


def merge(array, left, middle, right):
    i = left
    j = middle + 1
    for k in range(left,right + 1): 
        aux[k] = array[k]
    
    for k in range(left, right + 1):
        if i > middle: 
            array[k] = aux[j]
            j+=1
        elif j > right: 
            array[k] = aux[i] 
            i+=1
        elif aux[i] > aux[j]: 
            array[k] = aux[j]
            j+=1
        else: 
            array[k] = aux[i]
            i+=1

