import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2:{
        "Каа":{
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

# Добовляем информацию в словарь pets

def create():
    global pets
    # Получаем ключ
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1 # новый индификатор

    # запрашиваем данные о новом питомце
    name = input('Введите имя питомца: ')
    type = input('Введите тип питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner_neme = input('Введите имя владельца ')

    # Добовляем новую запись в словарь
    pets[new_id] = {
        'name': {
            'Вид питомца': type,
            'Возраст питомца': age,
            'Имя владельца': owner_neme
            }            
    }
    print(f'Питомец добавлен с ID: {new_id}')

def read(ID):
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        info = pet[name]
        suffix = get_suffix(info["Возраст питомца"])
        print(f"Это {info['Вид питомца']} по кличке \'{name}\'. "
              f"Возраст питомца: {info['Возраст питомца']} {suffix}."
              f"Имя владельца: {info['Имя владельца']}")
    else:
        print('питомец с таким ID не найден')


def update(ID):
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        print(f"Редактировние информации о {name}")
        new_name = input("Новая кличка: ") or name 
        new_type = input("Новый вид питомца: ") or pet[name]["Вид питомца"]
        new_age = input("Новый возраст: ") or pet[name]["Возраст питомца"]
        new_owner = input("Новое имя владельца: ") or pet[name]["Имя владельца"]
        
        pets[ID] = {
            new_name: {
                "Вид питомца": new_type,
                "Возраст питомца": int(new_age),
                "Имя владельца": new_owner
            }
        }
    else:
        print("Питомец не найден")

def delete(ID):
    if ID in pets:
        pets(ID).pop()
        print("Запись удалена")
    else:
        print("Питомец не найден")

# Вспомогательные функции

def get_pet(ID):
    return pets(ID) if ID in pets.keys()    else False

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <=4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"
    
def pets_list():
    for ID in pets:
        pet = pets[ID]
        name = list(pet.keys())[0]
        print(f"ID: {ID} - {name}")


# основной цикл программы
command = ""
while command.lower() != 'stop':
    command = input("\nВведите команду (create, read, update, delete, list) или 'stop' для выхода: ").lower()

    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == 'update':
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == 'delet':
        ID = int(input("Введите ID питомца: "))
        delete(ID)
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        print('Программа завершена')
    else:
        print("Неизвестная программа. Пожалуйста, введите reate, read, update, delete, list или 'stop' для выхода: ")
