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


class Item(object):
    # Corresponde a cada item dentro de um dicionário, possui os parâmetros chave e valor
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def __repr__(self):
        return "Key:{0} - Value:{1}".format(self.__key, self.__value)

    def getKey(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value


class Node(object):
    # Corresponde aos nós que compoem uma lista encadeada
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right


class Tree(object):
    # Árvore binária não balanceada
    def __init__(self):
        self.__root = None

    def insert(self, item):
        # Insere um elemento
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
        # Procura um elemento por meio de sua chave
        if self.__root is None:
            raise IndexError("Search on empty list")

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
        self.__removeAux(key, self.__root)

    def __removeAux(self, key, node):
        # Remove um elemento por meio de sua chave
        if node is None:
            raise IndexError("Remove from empty tree")

        if key < node.item.getKey():
            node.left = self.__removeAux(key, node.left)

        elif key > node.item.getKey():
            node.right = self.__removeAux(key, node.right)

        else:
            if node.left is None:
                aux = node
                node = node.right
                del aux

            elif node.right is None:
                aux = node
                node = node.left
                del aux

            else:
                node.left = self.__substitute(node, node.left)

        return node

    def __substitute(self, node, nodeR):
        # Encontra o antecessor de um valor para auxiliar na remoção de nós com 2 filhos
        if not(nodeR.right is None):
            nodeR.right = self.__substitute(node, nodeR.right)
        else:
            node.item = nodeR.item
            aux = nodeR
            nodeR = nodeR.left
            del aux

        return nodeR

    def inOrder(self):
        # Caminhamento em árvore binária
        self.__inOrderAux(self.__root)

    def __inOrderAux(self, root):
        if not (root is None):
            self.__inOrderAux(root.left)
            print(root.item)
            self.__inOrderAux(root.right)
