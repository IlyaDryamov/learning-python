pets = {}

num_pets = int(input('Сколько питомцев вы хотите добавить?'))

for i in range(num_pets):
    print(f'\nИнформация о питомце {i+1}:')
    pet_name = input('Введите имя питомца: ')
    pet_type = input('Введите тип питомца: ')
    pet_age = int(input('Введите возраст питомца: '))
    owner_neme = input('Введите имя владельца ')
# Добовляем информацию в словарь pets
    pets[pet_name] = {
        'Вид питомца': pet_type,
        'Возраст питомца': pet_age,
        'Имя владельца': owner_neme
    }
print('\nИмена всех питомцев (ключи словоря):')
for key in pets.keys():
    print(key)
# Выводим все значения (Информацию и питомцах)
print('\nИнформация о каждом питомце:')
for value in pets.values():
    print(value)
