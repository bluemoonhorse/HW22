import random
class NotADigit:
    pass

#Сортировка списка по возрастанию элементов в нем
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,

        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# 2 15 4 6 3 7 10
# 8
numbers =(input("Enter numbers separated by space: "))
your_number =int(input("Enter your number: "))

#выполнить проверку соответствия указанному в условии ввода данных.
check = numbers.split()

for char in check:
    try:
        if char.isdigit():
            pass
        else:
            pass
    except NotADigit as e:
        print("not a digit")

#Преобразование введённой последовательности в список
x = [int(i) for i in numbers.split()]
print(type(x))


# Сортировка списка по возрастанию элементов в нем
x = merge_sort(x)
print(x)

#модуль: "Допустим, что стоит такая же задача — найти индекс определённого элемента в массиве.
# В связи с тем, что алгоритм может искать только в отсортированном массиве",...
# я добавлю наше число в массив и отсортирую его
x.append(your_number)
print(x)
x = merge_sort(x)
print(x)

# и тогда бинарник заработает и будет давать позицию
# хотя возможно мне стоило добавить загаданное число сразу в массив но этого не было в техзадании
print("position: ", binary_search(x, your_number, 0, len(x)))


# Enter numbers separated by space: 2 15 4 6 3 7 10
# Enter your number: 8
# <class 'list'>
# [2, 3, 4, 6, 7, 10, 15]
# [2, 3, 4, 6, 7, 10, 15, 8]
# [2, 3, 4, 6, 7, 8, 10, 15]
# 5


