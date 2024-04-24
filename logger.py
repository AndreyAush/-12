from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    
    elif var == 2:
        with open('data_second_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n") 

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_var.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if  data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))     

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_var.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def update_data():
    name = name_data()
    data_first_list = read_file()

    record_to_update = list(filter(lambda x: (name) in x, data_first_list))
    if len(record_to_update) == 0:
        print('Запись не найдена')
        return
    print('Введите новые значения для записи: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    updated_record = f"{name} \n{surname} \n{phone} \n{address} \n \n"
    updated_index = data_first_list.index(record_to_update[0])
    data_first_list[updated_index] = updated_record
  

    write_file(data_first_list)

        



def delete_data():
    name = name_data()
    data_first_list = read_file()


    print(data_first_list)
    data_first_list = list(filter(lambda x: not(name) in x, data_first_list))
    print(data_first_list)


    write_file(data_first_list)