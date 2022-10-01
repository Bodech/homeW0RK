def int_input(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Вы ввели некорректное значение!')
        except Exception as error:
            print(f'Неизвестная ошибка: {type(error)} {error}!')
        else:
            return result


a = int_input('Введите первое число: ')
b = int_input('Введите второе число: ')
c = int_input('Введите третье число: ')


res_sum = a + b + c
res_min = a - b - c
res_mul = a * b * c

print(f"{a} + {b} + {c} = {res_sum}")
print(f"{a} - {b} - {c} = {res_min}")
print(f"{a} * {b} * {c} = {res_mul}")

try:
    res_div = a / b / c
    print(f"{a} / {b} / {c} = {res_div}")
except ZeroDivisionError:
    print("Невозможно поделить на 0!")
