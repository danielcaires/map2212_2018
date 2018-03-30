# -*- coding: utf-8 -*-
"""
========================Trabalho 2==========================
Disciplina: MAP 2212 - Laboratório de Simulação e Computação
Aluno: Daniel Oliveira Caires
Número USP: 5197211
Curso: Bacharelado em Matemática Aplicada e Computacional
Turma: 54 - Noturno
Período: 1o semestre de 2018
"""
import numpy as np

def retornaLadrilho(coordenadas):
  saida = [0,0]
  for i in range(2):
    saida[i] = int(coordenadas[i]*10)
  return saida[0],saida[1]


potenciasDeN = [5,10,15,20]
matrizLadrilhos = np.zeros((10,10)) #Matriz que contabiliza o numero de pontos por ladrilho

#repete o procedimento n vezes
for i in range(pow(2,5)):
  #Gera um par (x,y) de numeros pseudo-aleatorios em [0,1]X[0,1]
  ponto = np.random.rand(2)

  #Verifica em qual ladrilho o ponto (x,y) se encontra e contabiliza na matriz de ladrilhos
  ladrilho = retornaLadrilho(ponto)
  matrizLadrilhos[ladrilho[0]][ladrilho[1]]+=1

print matrizLadrilhos
#calcula a média, desvio padrão e Coeficiente de variação do número de pontos por ladrilho

#repete o experimento m vezes
#calcula a média dos Coeficientes de Variação e imprime

#Repete o procedimento para o próximo valor de n

