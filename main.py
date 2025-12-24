def bubble_sort(arr, ascending=True):
    """Сортировка пузырьком с выбором направления"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                # Для сортировки по возрастанию
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # Для сортировки по убыванию
                if arr[j] < arr[j + 1]:
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

    # Запрашиваем направление сортировки
    print("Выберите направление сортировки:")
    print("1 - по возрастанию")
    print("2 - по убыванию")

    choice = input("Введите 1 или 2: ")

    if choice == "1":
        sorted_numbers = bubble_sort(numbers.copy(), ascending=True)
        print("Числа, отсортированные по возрастанию:")
    elif choice == "2":
        sorted_numbers = bubble_sort(numbers.copy(), ascending=False)
        print("Числа, отсортированные по убыванию:")
    else:
        print("Неверный выбор! Сортировка по возрастанию.")
        sorted_numbers = bubble_sort(numbers.copy(), ascending=True)

    print(sorted_numbers)


if __name__ == "__main__":
    main()