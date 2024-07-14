first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для переменной first_result
first_result = (abs(len(s1) - len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))

# Генераторная сборка для переменной second_result без использования zip
second_result = [len(first[i]) == len(second[i]) if i < len(first) and i < len(second) else False for i in range(max(len(first), len(second)))]

# Вывод результатов
print(list(first_result))
print(list(second_result))
