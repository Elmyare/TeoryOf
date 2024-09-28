def multiply_column_style(num1, num2):
    # Преобразуем числа в строки, чтобы работать с ними поцифрово
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Обратим обе строки, чтобы легче было работать с ними в обратном порядке (с единиц)
    str_num1 = str_num1[::-1]
    str_num2 = str_num2[::-1]
    
    # Список для хранения промежуточных результатов
    partial_results = []

    # Для каждого разряда второго числа умножаем его на первое число
    for i, digit2 in enumerate(str_num2):
        carry = 0  # Для хранения остатка при умножении
        partial_result = []  # Текущий результат

        # Умножаем каждую цифру первого числа на текущую цифру второго
        for digit1 in str_num1:
            product = int(digit1) * int(digit2) + carry
            partial_result.append(str(product % 10))  # Добавляем младшую цифру
            carry = product // 10  # Остаток идет на следующий шаг

        if carry > 0:
            partial_result.append(str(carry))  # Добавляем остаток, если он есть

        # Преобразуем частичный результат обратно в строку и добавляем нули (сдвиг вправо)
        partial_result = ''.join(partial_result[::-1]) + '0' * i
        partial_results.append(partial_result)
    
    max_length = max(len(partial) for partial in partial_results)+1

    print(str_num1[::-1].rjust(max_length))
    print("x")
    print(str_num2[::-1].rjust(max_length))
    print("_"*max_length)
    
    for i, partial in enumerate(partial_results):
        print(partial.rjust(max_length))
        if i < len(partial_results)-1:
            print("+")

    print("_"*max_length)
    
    result = sum(int(partial) for partial in partial_results)
    print(str(result).rjust(max_length))
    return result

# Пример использования
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = multiply_column_style(num1, num2)
print(f"\nРезультат: {result}")
