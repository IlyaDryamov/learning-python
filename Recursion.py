def pe (list, index=0):
    #Ограничение конца списка
    if index == len(list):
        print('Конец списка')
        return
    
    print(list[index])

    pe(list, index + 1)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

pe(my_list)