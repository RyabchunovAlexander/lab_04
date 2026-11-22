from algopack.errors import ArgTypeError


def selection_sort(numbers):
    """Сортировка выбором. Возвращает новый список."""
    if not isinstance(numbers, (list, tuple)):
        raise ArgTypeError("Аргумент должен быть списком или кортежем")

    result = list(numbers)
    n = len(result)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result
