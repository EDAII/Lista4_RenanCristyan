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

# Retorna uma vetor aleatório
# Um vetor sem valores repetidos demora muito mais para ser criado
def random_list(size, max_value=None, repeat=True):
	if max_value == None or max_value < size:
		max_value = 10*size

	lista = []

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

def pop_heap(heap):
    swap(heap, 0, len(heap)-1)
    value = heap[len(heap)-1]

    del(heap[len(heap)-1])

    if len(heap) > 1:
        min_heapify(heap, (len(heap)//2)-1)

    return value

def heap_sort(vetor):
    min_heapify(vetor, (len(vetor)//2)-1)

    vetor_ordenado = []
    while vetor != []:
        vetor_ordenado.append(pop_heap(vetor))

    return vetor_ordenado

z = random_list(10)

print('vetor:')
print(z)
print('ordenado com heap sort:')
print(heap_sort(z))
