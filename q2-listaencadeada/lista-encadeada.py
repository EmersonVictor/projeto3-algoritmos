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

	def __repr__(self):
		return "Key:{0} - Value:{1}".format(self.__key,self.__value)

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
    def __init__(self,before=None,item=None,after=None):
        self.before = before
        self.item = item
        self.after = 

class Dictionary:
    #Implementação de um dicionário por meio de lista encadeada
    def __init__(self,first=None,last=None):
        self.__first = self.__last = Node()

    def empty(self):
        #Verifica se o dicionário está vazio e devolve um valor bool referente ao resultado
        if self.__last is self.__first:
            return True
        return False

    def insertStart(self, item):
        #Insere item no início
        aux = self.__first.after
        self.__first.after = Node(self.__first,item,self.__first.after)

        if self.empty():
            self.__last = self.__first.after
        else:
            aux.before = self.__first.after

    def insertEnd(self, item):
        #Insere item no fim
        self.__last = Node(self.__last,item,None)
        self.__last = self.__last.after

	def insertOrdered(self,item):
		#Insere um item de forma ordenada
		aux = self.__first.after
		while not(aux is None) and not(aux.item.getKey() > key):
			aux = aux.after

		if aux is None:
			self.__last.after = Node(self.__last, item, None)
			self.__last = self.__last.after
		else:
			aux.before.after = Node(aux.before,item,aux)
			aux.before = aux.before.after

    def removeStart(self):
        #Remove elemento do início
        if self.empty():
            raise IndexError ("Remove from empty list")

        aux = self.__first.after
        self.__first = aux.after

        if self.__first.after is self.__last:
            self.__last = self.__first
        else:
            aux.after.before = self.__first

        aux.after = aux.before = None
        del aux

    def removeEnd(self):
        #Remove elemento do fim
        if self.empty():
            raise IndexError ("Remove from empty list")

        aux = self.__last
        aux.before.after = aux.after
        self.__last = aux.before
        aux.before = None
        del aux

	def removeKey(self, key):
		#Remove elemento de acordo com uma chave
		if self.empty():
			raise IndexError ("Remove from empty list")

		aux = self.__first.after
		while not(aux is None) and not(aux.item.getKey() == key):
			aux = aux.after

		if aux is None:
			raise KeyError("Key not found")
		else:
			aux.before.after = aux.after
			if not (aux.after is None):
				aux.after.before = aux.before
			if self.__last is aux:
				self.__last = aux.before
			aux.after = aux.before = None
			del aux

	def searchKey(self, key):
		#Pesquisa elemento de acorco com uma chave
		if self.empty():
			raise IndexError ("Search on empty list")

		aux = self.__first.after
		while not(aux is None) and not(aux.item.getKey() == key):
			aux = aux.after

		if aux is None:
			raise KeyError("Key not found")
		else:
			return aux.item

	def printItems(self,start=1):
		#Imprime todos os elementos da lista na tela

		if self.empty() == True:
			raise IndexError("Print from empty list")

		aux = self.__first.after
		startAt = 1

		while startAt < start:
			if aux is None:
				raise IndexError("Index out of range")
			aux = aux.after
			startAt += 1

		while not(aux is None):
			print(aux)
			aux = aux.after
