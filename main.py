def bubble_sort_ascending(arr):
    """Сортировка пузырьком по возрастанию"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    print("Введите числа через пробел: ")
    numbers_input = input()

    # Преобразуем ввод в список чисел
    try:
        numbers = [float(num) for num in numbers_input.split()]
    except ValueError:
        print("Ошибка: введите только числа!")
        return

    # Сортируем по возрастанию (исходная версия)
    sorted_numbers = bubble_sort_ascending(numbers.copy())

    print("Числа, отсортированные по возрастанию:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()