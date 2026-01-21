n = int(input())
# создаем пустой список для хранения
nambers = []
# считываем п чисел, добовляем их в список
for i in range(n):
    num = int(input())
    nambers.append(num)
# переворачиваем список
nambers.reverse()

for num in nambers:
    print(num)