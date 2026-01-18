import math

x = int(input("Введите натуральное число"))
count = 0
# Запускаем цикл от 1 до корня из х
for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0: # Проверяем делится ли на i
        count += 1 # считаем делитель I
        if i != x //i: # Если i не равно x/i
            count += 1 # Учитываем парный делитеель

        print(count)
        