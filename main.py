def count_words_and_longest_word(input_string):
    try:

        words = input_string.split()


        word_count = len(words)
        longest_word = ""

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        return word_count, longest_word
    except Exception as e:
        return 0, str(e)


user_input = input("Введите строку: ")

count, longest = count_words_and_longest_word(user_input)
print("Количество слов в строке:", count)
if count > 0:
    print("Самое длинное слово:", longest)
else:
    print("Ошибка обработки строки.")