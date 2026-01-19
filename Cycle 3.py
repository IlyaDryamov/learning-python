a = int(input("Введите число а"))
b = int(input("Введите число б"))
# Создаем список для хранения чётных чисел
even_nambers = []
#  Запускаем счетчик от а до б
for num in range(a, b+1):
    if num % 2 == 0:
        even_nambers.append(str(num)) # преобразуем в строку
print(" ".join(even_nambers)) 