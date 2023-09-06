from random import randint


def binary_search(arr: list, start: int, stop: int, to_find: int):
    if start > stop:
        return 'Числа нет в массиве'
    else:
        pivot = (start + stop) // 2
        if to_find == arr[pivot]:
            return pivot
        else:
            if to_find > arr[pivot]:
                return binary_search(arr, pivot + 1, stop, to_find)
            else:
                return binary_search(arr, start, pivot - 1, to_find)


def main():
    print('Программа генерирует случайный массив из 100 цифр от 1 до 100\n'
          'и возвращает индекс искомого числа, если он есть в массиве')
    while True:
        try:
            to_find = int(input('Введите искомое число: '))
            break
        except:
            print('Принимаются только целые числа')
    arr = [randint(1, 100) for i in range(100)]
    arr.sort()
    print(binary_search(arr, 0, len(arr), to_find))


if __name__ == '__main__':
    main()
