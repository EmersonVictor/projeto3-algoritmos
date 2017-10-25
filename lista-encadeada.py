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

class Item:
    #Corresponde a cada item dentro de um dicionário, possui os parâmetros chave e valor
    def __init__(self,key,value):
        self.__key = key
        self.__value = value

    def getKey(self):
        return self.__key

    def setKey(self,key):
        self.__key = key

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.__value = value

class Node:
    #Corresponde aos nós que compoem uma lista encadeada
    def __init__(self,before=None,item=None,next=None):
        self.before = before
        self.item = item
        self.next = next

class Dictionary:
    #Implementação de um dicionário por meio de lista encadeada
    def __init__(self,raiz=None,first=None,last=None):
        self.__raiz = Node() = self.__first = self.__last

    def setFirst(self,node):
        return self.__first = node

    def setLast(self,node):
        return self.__last = node

    def empty(self):
        #Método que ver se o dicionário está vazio e devolve um valor bool referente ao resultado
        if self.__last is self.__first:
            return True
        return False
