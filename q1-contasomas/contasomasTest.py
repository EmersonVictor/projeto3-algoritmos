# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados

Autor:  Emerson Victor Ferreira da Luz (evfl)
Email:  evfl@cin.ufpe.br
Data: 2017-10-22

Copyright(c) 2017 Emerson Victor
'''
from time import perf_counter
from conta_somas import *
import numpy

MAX = 999999

class Cronometro:
   ''' Cronometra tempo gasto desde a criacao ate a chamada do metodo
       tempo_gasto
   '''
   def __init__(self):
      self.__criacao = perf_counter()
   def tempo_gasto(self):
      return perf_counter() - self.__criacao

def gera_seq_aleatoria(tam):
   return numpy.random.randint(-MAX,MAX, size=tam)

def main():
    resultados = open("cs-results.txt", "a+")
    seeds = [11,7,13,19,5189,7919]
    tam = [50,100,250,500,1000,1500]
    for i,seed in enumerate(seeds):
        numpy.random.seed(seed)
        vetor = gera_seq_aleatoria(tam[i])
        cron = Cronometro()
        total = countSums(vetor)
        resultado = "Tempo gasto com {0} elementos foi {1} segundos".format(tam[i],cron.tempo_gasto())
        print(resultado)
        resultados.write(resultado + "\n")
        del vetor
        del cron

    resultados.write("\n")
    resultados.close()

if __name__ == '__main__':
    for x in range(10):
        main()
