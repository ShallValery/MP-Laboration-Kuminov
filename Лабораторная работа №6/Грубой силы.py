import random
import time
def cr_arr(mass, len):
    for i in range(len):
        temp_list =[]
        for j in range(len):
            temp_num = random.randint(0, 10)
            temp_list.append(temp_num)
        mass.append(temp_list)
    
def square_Matrix_Mult(A,B):
    for i in range(n):
        for j in range (n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

n = int(input("Введите размер матриц: "))
A=[]
B=[]
C=[]
cr_arr(A, n)
print("Массив A:")
for i in range(n): print(A[i])
cr_arr(B, n)
print("Массив B:")
for i in range(n): print(B[i])
cr_arr(C, n)
square_Matrix_Mult(A,B)
print("Массив C:")
for i in range(n): print(C[i])
print("Время выполнения программы:: ", time.process_time())
