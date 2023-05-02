# 1) Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
# и возвращает введенное значение.
# Ввод текста вместо числа не должно приводить к падению приложения,
# вместо этого, необходимо повторно запросить у пользователя ввод данных.


def read_float():
    flag = False
    while not flag:
        number = input("Введите дробное число: ")
        try:
            number = float(number)
            flag = True
        except ValueError:
            print("Вы ввели не дробное число. Попробуйте еще раз.")
    return print("Ваше число:", number)


read_float()



# Разработайте программу, которая выбросит Exception,
# когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
EMPTY_STRING = "Вы ввели пустую строку. Попробуйте еще раз."


def isempty() -> str:
    flag = False
    while not flag:
        s = input("Введите строку:\n")
        if s and not s.isspace():
            flag = True
            return print("Ваша строка:", s)
        print(f'{ValueError(EMPTY_STRING)}')

isempty()

