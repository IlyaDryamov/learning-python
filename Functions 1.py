def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def create_factorial_list(input_number):
    # вычисляем факториал
    max_factorial = factorial(input_number)
    # создаем список факториалов
    factorial_list = []
    for i in range(max_factorial, 0, -1):
        factorial_list.append(factorial(i))
    return factorial_list

input_num = int(input('Введите натуральное целое число'))
result = create_factorial_list(input_num)
print(f'входное число: {input_num}')
print(f'факториал числа {input_num}: {factorial(input_num)}')
print(f'список факториалов: {result}')