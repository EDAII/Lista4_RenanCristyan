# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Heap Sort

from time import sleep
from random import randint
from copy import copy

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

def max_heapify(vetor, i):
    maior = i
    l = 2*i+1
    r = 2*i+2

    if l < len(vetor) and vetor[l] > vetor[maior]:
        maior = l
    
    if r < len(vetor) and vetor[r] > vetor[maior]:
        maior = r

    if maior != i:
        swap(vetor, i, maior)
        max_heapify(vetor, maior)

def min_heapify(vetor, i):
    menor = i
    l = 2*i+1
    r = 2*i+2

    if l < len(vetor) and vetor[l] < vetor[menor]:
        menor = l
    
    if r < len(vetor) and vetor[r] < vetor[menor]:
        menor = r

    if menor != i:
        swap(vetor, i, menor)
        min_heapify(vetor, menor)

def build(vetor, heap_type='min'):
    i = (len(vetor)//2)-1

    while i >= 0:
        if heap_type == 'min': min_heapify(vetor, i)
        if heap_type == 'max': max_heapify(vetor, i)
        i -= 1

def pop_heap(heap):
    value = heap[0]
    swap(heap, 0, len(heap)-1)

    del(heap[len(heap)-1])

    if len(heap) > 1:
        build(heap, heap_type='min')

    return value

def heap_sort(vetor):
    build(vetor, heap_type='min')

    vetor_ordenado = []
    while vetor != []:
        vetor_ordenado.append(pop_heap(vetor))

    return vetor_ordenado

def test_max_heap(heap, prints=False):
    i = 0

    while i < len(heap)//2:
        parent  = heap[i]
        left_c  = heap[i*2+1]
        if i*2+2 < len(heap):
            right_c = heap[i*2+2]
        else:
            right_c = None

        if prints:
            if right_c != None:
                print('parent = {}, left_c = {}, right_c = {}'.format(parent, left_c, right_c))
            else:
                print('parent = {}, left_c = {}'.format(parent, left_c))
        else:
            try:
                if right_c != None:
                    assert parent >= left_c and parent >= right_c
                else:
                    assert parent >= left_c
            except AssertionError:
                print('MAX HEAP ERROR')
                print('p = {}, l = {}, r = {}'.format(parent, left_c, right_c))
                exit(1)
        
        i += 1

    print('MAX HEAP OK')

def test_min_heap(heap, prints=False):
    i = 0

    while i < len(heap)//2:
        parent  = heap[i]
        left_c  = heap[i*2+1]
        if i*2+2 < len(heap):
            right_c = heap[i*2+2]
        else:
            right_c = None

        if prints:
            if right_c != None:
                print('parent = {}, left_c = {}, right_c = {}'.format(parent, left_c, right_c))
            else:
                print('parent = {}, left_c = {}'.format(parent, left_C))
        else:
            try:
                if right_c != None:
                    assert parent <= left_c and parent <= right_c
                else:
                    assert parent <= left_c
            except AssertionError:
                print('MIN HEAP ERROR')
                print('p = {}, l = {}, r = {}'.format(parent, left_c, right_c))
                exit(1)
        
        i += 1
    
    print('MIN HEAP OK')

z = random_list(16)
min_h = copy(z)
max_h = copy(z)

print('vetor:')
print(z)
print('-'*25)

print('min_heap')
build(min_h, heap_type='min')
print(min_h)
test_min_heap(min_h)
print('-'*25)

print('max_heap')
build(max_h, heap_type='max')
print(max_h)
test_max_heap(max_h)
print('-'*25)

print('vetor ordenado')
ordenado = heap_sort(z)
print(ordenado)
print('-'*25)