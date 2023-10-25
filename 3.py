try:
    n, m = map(int, input("Введите количество строк и столбцов (n m): ").split())

    matrix = []
    print("Введите элементы массива:")
    for i in range(n):
        row = []
        for j in range(m):
            try:
                element = int(input(f"Введите элемент массива [{i}][{j}]: "))
                row.append(element)
            except ValueError:
                print("Ошибка: Введите целое число.")
                break
        else:
            matrix.append(row)

    print("Исходный массив:")
    for row in matrix:
        print(*row)

    i, j = map(int, input("Введите номера столбцов i и j для обмена (разделите пробелом): ").split())

    if 0 <= i < m and 0 <= j < m:
        for row in matrix:
            row[i], row[j] = row[j], row[i]

        print("Результат обмена столбцов:")
        for row in matrix:
            print(*row)
    else:
        print("Неверные номера столбцов. Пожалуйста, убедитесь, что номера находятся в допустимых пределах.")

except ValueError:
    print("Ошибка: Введите целое число для количества строк и столбцов.")
