def remove_word(word):  # Функция "переворачивает" слово, оставляя на месте отличные цифры и иные символы
    if type(word) != str:  # Проверяет тип данных аргумента функции
        raise TypeError("Expected only string")
    final_string = []
    for case in word.split(' '):
        list_of_letter = [c for c in case if c.isalpha()]
        position_of_exceptions = {i: c for (i, c) in enumerate(case) if not c.isalpha()}
        revers_word = list_of_letter[::-1]
        [revers_word.insert(key, position_of_exceptions[key]) for key in position_of_exceptions]
        final_string.append(''.join(revers_word))
    return ' '.join(final_string)


if __name__ == '__main__':
    case = input()
    print(' '.join([remove_word(word) for word in case.split(' ')]))
