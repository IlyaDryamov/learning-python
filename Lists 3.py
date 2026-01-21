m = int(input("Введите максимальную грузоподъёмность лодки"))
n = int(input("Введите к-во рыбоков"))
mass = []
for i in range(n):
    i = int(input("Введите массу рыбака"))
    if m > i:
        mass.append(i)
    else:
        print("Извини, братан, лодка с тобой потонет")
mass.sort()
left = 0
right = len(mass) - 1
# запускаем счетчик лодок
boat = 0
while left <= right:
    if mass[left] + mass[right] <= m:
        left += 1
        right -= 1
        boat += 1
print(f"количество лодок, которые понадобятся: {boat}")