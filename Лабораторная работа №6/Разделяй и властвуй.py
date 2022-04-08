import random
import time

def foo(matrix, quater):
    l1 = len(matrix)//2
    l2 = len(matrix[0])//2
 
    if quater == 1:
        A11 = []
        for line in matrix[:l1]:
            A11.append(line[:l2])
        return A11
 
    if quater == 2:
        A12 = []
        for line in matrix[:l1]:
            A12.append(line[l2:])
        return A12
 
    if quater == 3:
        A21 = []
        for line in matrix[l1:]:
            A21.append(line[:l2])
        return A21

    if quater == 4:
        A22 = []
        for line in matrix[l1:]:
            A22.append(line[l2:])
        return A22

def matrix_sum(A, B):
    for i in range(len(A)):     
        for j in range(len(A[0])): 
            A[i][j] = A[i][j] + B[i][j]
    return A

def Square_Matrix_Multiple_Recurs(A, B): 
    if len(A) == 1:
        C = [[]]
        C[0].append(A[0][0] * B[0][0])
        return C
   
    C = []
    C11 = matrix_sum(Square_Matrix_Multiple_Recurs(foo(A, 1), foo(B, 1)), Square_Matrix_Multiple_Recurs(foo(A, 2), foo(B, 3)))

    for i in range(len(C11)):
        C.append(C11[i])

    C12 = matrix_sum(Square_Matrix_Multiple_Recurs(foo(A, 1), foo(B, 2)), Square_Matrix_Multiple_Recurs(foo(A, 2), foo(B, 4)))

    for i in range(len(C12)):
        for j in range(len(C12)):
            C[i].append(C12[i][j])

    C21 = matrix_sum(Square_Matrix_Multiple_Recurs(foo(A, 3), foo(B, 1)), Square_Matrix_Multiple_Recurs(foo(A, 4), foo(B, 3)))

    for i in range(len(C21)):
        C.append(C21[i])

    C22 = matrix_sum(Square_Matrix_Multiple_Recurs(foo(A, 3), foo(B, 2)), Square_Matrix_Multiple_Recurs(foo(A, 4), foo(B, 4)))

    if len(C)//2 == 1:
        C[1].append(C22[0][0])     
        
    else:   
       for i in range(len(C22)):
           for j in range(len(C22)):
               C[i + len(C22)].append(C22[i][j])

    return C

N = int(input("Введите размер матрицы: "))
A = []
B = []

for i in range(N):
    A_row = []
    B_row = []
    for j in range(N):
        A_row.append(random.randint(-10, 10))
        B_row.append(random.randint(-10, 10))
    A.append(A_row)
    B.append(B_row)

print("Матрица A:")

for i in range(N):
    print(A[i])

print()
print("Матрица B:")

for i in range(N):
    print(B[i])

C = Square_Matrix_Multiple_Recurs(A, B)

print()
print("Matrix C: ")

for i in range(N):
    print(C[i])
    
print("Время выполнения программы:: ", time.process_time())

