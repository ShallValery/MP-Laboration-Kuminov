import random
import time
def quicksort(mas, low, high):
    if low < high:
        p = partition(mas, low, high)
        quicksort(mas, low, p)
        quicksort(mas, p + 1, high)
 
 
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high - 1
 
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
 
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[low], arr[j] = arr[j], arr[low]
            return j
 
 
n = int(input('Введите длину массива: '))
Array = [random.randint(10, 99) for i in range(n)]
print('Исходный массив: ', Array)
quicksort(Array, 0, len(Array))
print("Время сортировки: ", time.process_time(),"\n")
print(Array)

