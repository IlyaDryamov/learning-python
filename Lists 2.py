n = int(input())
# считываем массив из строки
a = list(map(int,input().split()))
# объединяем последний эл-т и остаток массива
result = [a[-1]] + a[:-1]
print(' '.join(map(str, result)))
