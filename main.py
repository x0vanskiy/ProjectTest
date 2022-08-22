while True:
    list1 = [11111111111, 123739272946, 249372938294]
    list2 = [994 - 3596706464, 994 - 2374600505, 994 - 1942095656]
    choose = int(input(
        "1)Отсортировать по идентификацыонным кодам\n2)Отсортировать по номер телефона\n3)Вывести список пользователей с кодами и теле\n4)Выход-"))

    if choose == 1:
        list1.sort()
        print(list1)

    elif choose == 2:
        list2.sort()
        print(list2)

    elif choose == 3:
        print(list1, list2)

    elif choose == 4:
        print("Exit")
        break


    else:
        print("")