import random
import time

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(Array, ind, size):
    l = left(ind)
    r = right(ind)
    if (l < size and Array[l] > Array[ind]):
        largest = l
    else:
        largest = ind
    if (r < size and Array[r] > Array[largest]):
        largest = r
    if (largest != ind):
        Array[largest], Array[ind] = Array[ind], Array[largest]


def build_max_heap(Array):
    length = len(Array)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(Array, ind=start, size=length)
        start = start - 1


def heapsort(Array):
    build_max_heap(Array)
    for i in range(len(Array) - 1, 0, -1):
        Array[0], Array[i] = Array[i], Array[0]
        max_heapify(Array, ind=0, size=i)


lengthArray = int(input('Введите длину массива: '))
Array = [random.randint(10, 99) for i in range(lengthArray)]
print('Исходный массив: ', Array)

heapsort(Array)
print('Отсортированный массив: ', Array)

print("Время сортировки: ", time.process_time(),"\n")
