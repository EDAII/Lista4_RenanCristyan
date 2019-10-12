# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Heap Sort

from random import randint
from copy import copy
import heapq

def swap(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

# Retorna uma vetor aleatório de tamanho size + 1 (a posição 0 não é usada no heap)
# Um vetor sem valores repetidos demora muito mais para ser criado
def random_list(size, max_value=None, repeat=True):
	if max_value == None or max_value < size:
		max_value = 10*size

	lista = [0]

	i = 0
	while i < size:
		num = randint(0,max_value)
		
		if repeat:
			lista.append(num)
			i += 1
		else:
			if num not in lista:
				lista.append(num)
				i += 1

	return lista

def min_heapify(vetor, i): # i = indice do vetor v[i]
    # Considerar o caso que só tem o nó da esquerda:
    if 2*i+2 >= len(vetor):
        l, li = vetor[2*i+1], 2*i+1    
        menor, menori = l, li

    else:
        l, li = vetor[2*i+1], 2*i+1
        r, ri = vetor[2*i+2], 2*i+2
        menor, menori = -1, -1

        if l < r:
            menor = l
            menori = li
        else:
            menor = r
            menori = ri

    if menor < vetor[i]:
        swap(vetor, i, menori)
        
        if 2*menori+2 >= len(vetor):
            if menori < len(vetor)//2:
                if vetor[menori] > vetor[2*menori+1]:
                    min_heapify(vetor, menori)
        elif vetor[menori] > vetor[2*menori+1] or vetor[menori] > vetor[2*menori+2]:
            min_heapify(vetor, menori)

    if i != 0:
        min_heapify(vetor, i-1)

    return vetor

z = random_list(10)
print('vetor = \t\t', z[1:])

zi = copy(z)
za = min_heapify(z, (len(z)//2)-1)
heapq.heapify(zi)

print('heapq.heapify() = \t', zi[1:])
print('min_heapify() = \t', za[1:])