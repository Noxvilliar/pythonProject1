import math

def process_data(data):
    if isinstance(data, dict):
        # Сортировка словаря  возрастания и убывания
        sorted_ascending = dict(sorted(data.items(), key=lambda item: item[1]))
        sorted_descending = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return sorted_ascending, sorted_descending
    elif isinstance(data, list):
        # буквы и чисела в списке
        letter_count = sum(1 for item in data if isinstance(item, str) and item.isalpha())
        number_count = sum(1 for item in data if isinstance(item, (int, float)))
        return letter_count, number_count
    elif isinstance(data, (int, float)):
        # простое число
        if data <= 1:
            return "Число не является простым"
        for i in range(2, int(math.sqrt(data)) + 1):
            if data % i == 0:
                return "Число не является простым"
        return "Число является простым"
    elif isinstance(data, str):
        # Поиск всех палиндромов в строке
        words = data.split()
        palindromes = [word for word in words if word == word[::-1]]
        return palindromes
    else:
        return "Тип данных не поддерживается"

def get_valid_input(data_type):
    while True:
        try:
            if data_type == "dict":
                data = eval(input("Введите словарь: "))
                if not isinstance(data, dict):
                    raise ValueError()
            elif data_type == "list":
                data = eval(input("Введите список: "))
                if not isinstance(data, list):
                    raise ValueError()
            elif data_type == "number":
                data = eval(input("Введите число: "))
                if not isinstance(data, (int, float)):
                    raise ValueError()
            elif data_type == "string":
                data = input("Введите строку: ")
                if not isinstance(data, str):
                    raise ValueError()
            else:
                print("Неподдерживаемый тип данных")
                continue

            return data
        except (ValueError, NameError):
            print("Ошибка: Некорректные данные. Пожалуйста, введите корректные данные.")

def main():
    data_type = input("Выберите тип данных (dict, list, number, string) для ввода: ")

    data = get_valid_input(data_type)
    result = process_data(data)

    if isinstance(result, tuple):
        print("Словарь (по возрастанию):", result[0])
        print("Словарь (по убыванию):", result[1])
        print("Количество букв:", result[0])
        print("Количество чисел:", result[1])
    else:
        print(result)

if __name__ == "__main__":
    main()
