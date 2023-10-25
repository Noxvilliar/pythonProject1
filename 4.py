try:

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))


    result = num1 / num2


    print("Результат деления: ", result)

except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")

except ValueError:
    print("Ошибка: Введено некорректное число!")

finally:
    print("Программа завершена.")