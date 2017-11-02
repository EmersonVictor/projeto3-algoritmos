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
from arvore_binaria import *
sys.path.append('../testes')
from listaVeiculos import *


def newTree(ordered=False, reverse=False):
    # Cria um objeto do tipo árvore não ordenado ou ordenado crescentemente/decrescentemente
    tree = Tree()
    auxArray = createList("../testes/veiculos.txt")

    if ordered is False:
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            tree.insert(item)

    elif ordered is True and reverse is False:
        auxArray = sorted(auxArray, key=lambda x: x.getPlaca())
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            tree.insert(item)

    elif ordered is True and reverse is True:
        auxArray = sorted(auxArray, key=lambda x: x.getPlaca(), reverse=True)
        for i in auxArray:
            item = Item(i.getPlaca(), i)
            tree.insert(item)

    return tree


def timeSearch(tree, key):
    # Calcula o tempo de busca de uma determinada chave em uma árvore
    start = timeit.default_timer()
    tree.search(key)
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
    tree = newTree()
    keys = keysToSearch(57, 1000)
    results = open("tr-results.txt", "a+")
    results.write("TESTE NÃO ORDENADO\n\n")
    print("TESTE NÃO ORDENADO\n\n")

    for key in keys:
        time = timeSearch(tree, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.write("\n")
    tree = newTree(True)
    results.write("TESTE ORDENADO CRESCENTEMENTE\n\n")
    print("TESTE ORDENADO CRESCENTEMENTE\n\n")

    for key in keys:
        time = timeSearch(tree, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.write("\n")
    tree = newTree(True, True)
    results.write("TESTE ORDENADO DECRESCENTEMENTE\n\n")
    print("TESTE ORDENADO DECRESCENTEMENTE\n\n")

    for key in keys:
        time = timeSearch(tree, key)
        time = "{0}\n".format(time)
        results.write(time)
        print(time)

    results.close()


if __name__ == "__main__":
    main()
