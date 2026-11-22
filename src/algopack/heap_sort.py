from algopack.errors import ArgTypeError


def heapify(numbers, heap_size, i):
    """Восстановление свойства максимальной кучи."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and numbers[left] > numbers[largest]:
        largest = left

    if right < heap_size and numbers[right] > numbers[largest]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, heap_size, largest)


def heap_sort(numbers):
    """Пирамидальная сортировка по возрастанию."""
    if not isinstance(numbers, (list, tuple)):
        raise ArgTypeError("Аргумент должен быть списком или кортежем")

    result = list(numbers)
    n = len(result)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    # Перемещение максимальных элементов в конец списка
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(result, i, 0)

    return result
