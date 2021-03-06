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
import linecache
import timeit
import sys
import numpy
from lista_encadeada import *
sys.path.append('../testes')
from listaVeiculos import *


def newList(ordered=False, reverse=False):
    # Cria um objeto do tipo dicionário não ordenado ou ordenado crescentemente/decrescentemente
    array = Dictionary()
    auxArray = createList("../testes/veiculos.txt")

    if ordered is False:
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            array.insertStart(item)

    elif ordered is True and reverse is False:
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            array.insertOrdered(item)

    elif ordered is True and reverse is True:
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            array.insertOrdered(item, True)

    return array


def timeSearch(dictionary, key):
    # Calcula o tempo de busca de uma determinada chave em um dicionário
    start = timeit.default_timer()
    dictionary.searchKey(key)
    end = timeit.default_timer()
    return end - start


def keysToSearch(seed, size):
    # Cria uma lista de placas a partir do arquivo de veículos
    numpy.random.seed(seed)
    array = list(numpy.random.randint(0, 20000, size=size))
    keys = []

    for position in array:
        aux = linecache.getline("../testes/veiculos.txt", position).split()
        keys.append(aux[6])

    return keys


def main():
    dictionary = newList()
    keys = keysToSearch(57, 1000)
    results = open("ls-results.txt", "a+")
    results.write("TESTE NÃO ORDENADO\n\n")
    print("TESTE NÃO ORDENADO\n\n")

    for key in keys:
        time = timeSearch(dictionary, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.write("\n")
    dictionary = newList(True)
    results.write("TESTE ORDENADO CRESCENTEMENTE\n\n")
    print("TESTE ORDENADO CRESCENTEMENTE\n\n")

    for key in keys:
        time = timeSearch(dictionary, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.write("\n")
    dictionary = newList(True, True)
    results.write("TESTE ORDENADO DECRESCENTEMENTE\n\n")
    print("TESTE ORDENADO DECRESCENTEMENTE\n\n")

    for key in keys:
        time = timeSearch(dictionary, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.close()


if __name__ == "__main__":
    main()
