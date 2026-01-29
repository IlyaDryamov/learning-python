import collections

pets = {}

# Добовляем информацию в словарь pets

def create():
    global pets
    # Получаем ключ
    last = collections.deque(pets.key(), maxlen=1)
    new_id = last + 1 # новый индификатор

    # запрашиваем данные о новом питомце
    pet_name = input('Введите имя питомца: ')
    pet_type = input('Введите тип питомца: ')
    pet_age = int(input('Введите возраст питомца: '))
    owner_neme = input('Введите имя владельца ')

    # Добовляем новую запись в словарь
    pets[new_id] = {
        'Имя питомца': pet_name,
            'Вид питомца': pet_type,
            'Возраст питомца': pet_age,
            'Имя владельца': owner_neme
            
    }
    print(f'Питомец добавлен с ID: {new_id}')

def read():
    new_id = int(input('Введите ID питомца для просмотра: '))
    if new_id in pets:
        pets = pets[new_id]
        print.values(f'ID питомца {new_id}'
              f'Это {pets['Вид питомца']} по кличке '{pets['Имя питомца']}.'
              f'Возраст питомца: {pets['Возраст питомца']}.'
              f'Имя владельца: {['Имя владельца']}')
    else:
        print('питомец с таким ID не найден')

# основной цикл программы
while command != 'stop':
    command = input('\nВведите команду (create, read, update, delete) или 'stop' для выхода: ').lower()

    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delet':
        delete()
    elif command == 'stop':
        print('Программа завершена')
    else:
        print('Неизвестная программа. Пожалуйста введите reate, read, update, delete или 'stop' для выхода: ')
