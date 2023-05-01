# 1) Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности
# элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.


def difference_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print(RuntimeError("Длины массивов не равны"))
        return None
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])
    return result


# 2) Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен частному
# элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.


def divide_arrs(arr1, arr2):
    if len(arr1) != len(arr2):
        print(RuntimeError("Длины массивов не равны"))
        return None
    result = []
    for i in range(len(arr1)):
        if arr2[i] == 0:
            print(ZeroDivisionError("На ноль делить нельзя!"))
            return None
        result.append(arr1[i] / arr2[i])
    return result


# 3) Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен сумме
# элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.


def sum_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print(RuntimeError("Длины массивов не равны"))
        return None
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result


arr_A = [0, 90, 109, 12]
arr_B = [1, 5, 3, 1]
print("Разность:", difference_arrays(arr_A, arr_B))
print("Деление:", divide_arrs(arr_A, arr_B))
print("Сумма:", sum_arrays(arr_A, arr_B))
