dict = {}
for k in range (10, -6, -1):
    if k != 0: # пропускаем 0
        dict[k] = k ** k
print(dict)