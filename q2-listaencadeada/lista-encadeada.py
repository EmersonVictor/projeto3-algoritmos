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
    def __init__(self,before=None,item=None,next=None):
        self.before = before
        self.item = item
        self.next = next

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
        aux = self.__first.next
        self.__first.next = Node(self.__first,item,self.__first.next)

        if self.empty():
            self.__last = self.__first.next
        else:
            aux.before = self.__first.next

    def insertEnd(self, item):
        #Insere item no fim
        self.__last = Node(self.__last,item,None)
        self.__last = self.__last.next

	def insertOrdered(self,item):
		#Insere um item de forma ordenada
		aux = self.__first.next
		while not(aux is None) and not(aux.item.getKey() > key):
			aux = aux.next

		if aux is None:
			self.__last.next = Node(self.__last, item, None)
			self.__last = self.__last.next
		else:
			aux.before.next = Node(aux.before,item,aux)
			aux.before = aux.before.next

    def removeStart(self):
        #Remove elemento do início
        if self.empty():
            raise IndexError ("Remove from empty list")

        aux = self.__first.next
        self.__first = aux.next

        if self.__first.next is self.__last:
            self.__last = self.__first
        else:
            aux.next.before = self.__first

        aux.next = aux.before = None
        del aux

    def removeEnd(self):
        #Remove elemento do fim
        if self.empty():
            raise IndexError ("Remove from empty list")

        aux = self.__last
        aux.before.next = aux.next
        self.__last = aux.before
        aux.before = None
        del aux

	def removeKey(self, key):
		#Remove elemento de acordo com uma chave
		if self.empty():
			raise IndexError ("Remove from empty list")

		aux = self.__first.next
		while not(aux is None) and not(aux.item.getKey() == key):
			aux = aux.next

		if aux is None:
			raise KeyError("Key not found")
		else:
			aux.before.next = aux.next
			if not (aux.next is None):
				aux.next.before = aux.before
			if self.__last is aux:
				self.__last = aux.before
			aux.next = aux.before = None
			del aux

	def searchKey(self, key):
		#Pesquisa elemento de acorco com uma chave
		if self.empty():
			raise IndexError ("Search on empty list")

		aux = self.__first.next
		while not(aux is None) and not(aux.item.getKey() == key):
			aux = aux.next

		if aux is None:
			raise KeyError("Key not found")
		else:
			return aux.item

	def printItems(self,start=1):
		#Imprime todos os elementos da lista na tela

		if self.empty() == True:
			raise IndexError("Print from empty list")

		aux = self.__first.next
		startAt = 1

		while startAt < start:
			if aux is None:
				raise IndexError("Index out of range")
			aux = aux.next
			startAt += 1

		while not(aux is None):
			print(aux)
			aux = aux.next
