import time
import numpy as np

def make_arr(len_arr):
    return np.random.randint(-100, 100, len_arr)

def find_max_crossing_subarray(a, low, mid, high):
    max_left = 0
    left_sum = -1e308
    summ = 0
    for i in range(mid, low - 1, -1):
        summ += a[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
            
    max_right = 0
    right_sum = -1e308
    summ = 0
    for j in range(mid + 1, high + 1, 1):
        summ += a[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
            
    return max_left, max_right, left_sum + right_sum

def find_max_subarray(a, low, high): 
    if high == low:
        return low, high, a[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = find_max_subarray(a, low, mid)
        right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum   

def find_max_subarray_brutefoce(a):
    max_sum = 0
    max_low = 0
    max_high = 0
    for i in range(0, len(a)):
        summ = 0
        for j in range(i, len(a)):
            summ += a[j]
            if summ > max_sum:
                max_sum = summ
                max_low = i
                max_high = j
    return max_low, max_high, max_sum

len_arr = int(input("Введите длинну массива: "))

arr = make_arr(len_arr)
print("Был сформирован следующий массив, длиной ",len_arr,":\n",arr,"\n")
print("Каким способом найти максимальный подмассив?\n")
n = int(input("Введите 1 для метода полного перебора или 2 для метода Разделяй и властвуй "))

if n == 1:
    l1, r1, s1 = find_max_subarray_brutefoce(arr)
    print("\n",arr[l1:r1+1])
    print("\nВремя поиска максимального подмассива путем полного перебора: \n", time.process_time(),"\n")
    print('Начало и конец подмассива = {0}, длинна подмассива = {1}, сумма = {2}'.format((l1, r1), len(arr[l1:r1+1]), s1),"\n")
if n == 2:
    l2, r2, s2 = find_max_subarray(arr, 0, len(arr) - 1)
    print(arr[l2:r2+1])
    print("Время поиска максимального подмассива путем алгоритма Разделяй и властвуй: ", time.process_time(),"\n")
    print('Начало и конец подмассива = {0}, длинна подмассива = {1}, сумма = {2}'.format((l2, r2), len(arr[l2:r2+1]), s2),"\n")
if n > 2:   
    print("Вы ввели неверный символ")
