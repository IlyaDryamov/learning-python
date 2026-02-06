import random

# создаем матрицы заданного размера
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [random.randint(-200, 200) for j in range(cols)] # Генерируем числа от -200 до 200
        matrix.append(row)
    return matrix

# сложение 2 матриц
def add_matrices(matrix1, matrix2):
    res =[]
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        res.append(row)
    return res

# создаем 2 матрицы
rows, cols = 10, 10
matrix1 = create_matrix(rows, cols)
matrix2 = create_matrix(rows, cols)

# Складываем матрицы
matrix3 = add_matrices(matrix1, matrix2)

# для красивого вывода матрицы
def p_m(matrix):
    for row in matrix:
        print(row)
    print()

print("Матрица 1: ")
p_m(matrix1)

print("Матрица 2: ")
p_m(matrix2)

print("Матрица 3: ")
p_m(matrix3)