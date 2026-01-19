line = input("Введите слово").strip()
# Проверяем, являются ли строки палиндромом. И сравниваем ее с обратной
if line == line[::-1]:
    print ("yes")
else:
    print("no")