import time 
import random

# Функция деления списка на подмассивы
def Breakdown(A, b, c): 
    if c - b > 1:
        d = (b + c)//2
        Breakdown(A, b, d)
        Breakdown(A, d, c)
        Sort(A, b, c, d)
 
# Функция сортировки
def Sort(A, b, c, d): 
    left = A[b:d]
    right = A[d:c] 
    k = b
    i = 0
    j = 0
    while (b + i < d and d + j < c): 
        # Если элемент из левого массива меньше чем из правого, тогда:
        if (left[i] <= right[j]): 
            A[k] = left[i]
            i = i + 1
        # Иначе помещаем элемент из правого массива в отсортированный
        else: 
            A[k] = right[j]
            j = j + 1
        k = k + 1
    # Когда добрались до конца левого массива
    if b + i < d: 
        while k < c:
            A[k] = left[i]
            i = i + 1
            k = k + 1
    # Когда добрались до конца правого массива
    else: 
        while k < c:
            A[k] = right[j]
            j = j + 1
            k = k + 1
 
# Создание списка случайных элементов
l = int(input("Введите длину сортируемого списка: ")) 
My_Sort_list = []
for i in range(0, l): 
    rand = random.randint(0, 100)
    My_Sort_list.append(rand)
print("Будет отсортирован следующий список: ", My_Sort_list)

# Вызываем функцию деления списка на подмассивы длиной 1
Breakdown(My_Sort_list, 0, len(My_Sort_list))

print("Отсортированный массив: ", My_Sort_list)
print("Время выполнения программы:: ", time.process_time())
