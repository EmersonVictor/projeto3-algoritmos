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
class Item(object):
    #Corresponde a cada item dentro de um dicionário, possui os parâmetros chave e valor
    def __init__(self,key,value):
        self.__key = key
        self.__value = value

	def __repr__(self):
		return "Key:{0} - Value:{1}".format(self.__key,self.__value)

    def getKey(self):
        return self.__key

    def setKey(self,key):
        self.__key = key

    def getValue(self):
        return self.__value

    def setValue(self,value):
        self.__value = value

class Node(object):
    #Corresponde aos nós que compoem uma lista encadeada
    def __init__(self,left=None,item=None,right=None):
        self.left = left
        self.item = item
        self.right = right

class Tree(object):
    #Árvore binária não balanceada
    def __init__(self,root):
        self.__root = None

    def insert(self,item):
        #Insere um elemento
        if self.__root is None:
            self.__root = Node(None, item, None)
            return

        aux = self.__root
        while True:
            if item.getKey() < aux.item.getKey():
                if aux.left is None:
                    aux.left = Node(None, item, None)
                    return
                aux = aux.left
            elif item.getKey() > aux.item.getKey():
                if aux.right is None:
                    aux.right = Node(None, item, None)
                    return
                aux = aux.right
            else:
                aux.item.setValue(item.getValue())
                return

    def search(self, key):
        #Procura um elemento por meio de sua chave
        if self.__root is None:
            raise IndexError ("Search on empty list")

        aux = self.__root
        while True:
            if key < aux.item.getKey():
                if aux.left is None:
                    raise KeyError("Key not found")
                aux = aux.left
            elif key > aux.item.getKey():
                if aux.right is None:
                    raise KeyError("Key not found")
                aux = aux.right
            else:
                return aux.item

    def remove(self, key):
        #Remove um elemento por meio de sua chave
        if self.__root is None:
            raise IndexError ("Remove from empty list")

        rootAux = None
        aux = self.__root
        while not(aux is None):
            if key < aux.item.getKey():
                rootAux = aux
                aux = aux.left
            elif key > aux.item.getKey():
                rootAux = aux
                aux = aux.right
            else:
                if aux.left is None and aux.right is None:
                    rootAux = None
                    del aux
                    return
                elif aux.left is None and not(aux.right is None):
                    rootAux = aux.right
                    aux.right = None
                    del aux
                    return
                elif not(aux.right is None) and aux.right is None:
                    rootAux = aux.left
                    aux.left = None
                    del aux
                    return
                else:
                    replace = self.__substitute(aux)
                    rootAux = replace
                    replace.right = aux.right
                    replace.left = aux.left
                    aux.left = aux.right = None
                    del aux

    def __substitute(self, node):
        #Encontra o antecessor de um valor para auxiliar na remoção de nós com 2 filhos
        rootAux = None
        aux = node.left

        while not (aux.right is None):
            rootAux = aux
            aux = aux.right

        rootAux = aux.right
        return aux

    def inOrder(self, root=self.root):
        #Caminhamento em árvore binária
        if not (root is None):
            self.inOrder(root.left)
            print(root.item)
            self.inOrder(root.right)
