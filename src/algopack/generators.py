import random

from algopack.errors import ArgTypeError, ArgValueError


def generate_random(n, seed=None, low_bound=-1000, high_bound=1000):
    """Создаёт список случайных целых чисел."""
    if (type(n) is not int or type(low_bound) is not int
            or type(high_bound) is not int):
        raise ArgTypeError("Размер и границы должны быть целыми числами")

    if seed is not None and type(seed) is not int:
        raise ArgTypeError("Seed должен быть целым числом")

    if n < 0:
        raise ArgValueError("Размер массива не может быть отрицательным")

    if low_bound > high_bound:
        raise ArgValueError("Нижняя граница больше верхней")

    rng = random.Random(seed)
    return [rng.randint(low_bound, high_bound) for _ in range(n)]


def generate_sorted(n, seed=None, low_bound=-1000, high_bound=1000):
    """Создаёт список, отсортированный по возрастанию."""
    result = generate_random(n, seed, low_bound, high_bound)
    result.sort()
    return result


def generate_reversed(n, seed=None, low_bound=-1000, high_bound=1000):
    """Создаёт список, отсортированный по убыванию."""
    result = generate_random(n, seed, low_bound, high_bound)
    result.sort(reverse=True)
    return result


def generate_almost_sorted(n, seed=None, low_bound=-1000, high_bound=1000):
    """Создаёт почти отсортированный список."""
    result = generate_random(n, seed, low_bound, high_bound)
    result.sort()

    rng = random.Random(seed)

    if n > 1:
        for _ in range(max(1, n // 20)):
            i = rng.randrange(n)
            j = rng.randrange(n - 1)

            if j >= i:
                j += 1

            result[i], result[j] = result[j], result[i]

    return result


def generate_with_duplicates(n, seed=None, low_bound=-1000,
                             high_bound=1000, unique_count=5):
    """Создаёт список с большим количеством повторений."""
    if (type(n) is not int or type(low_bound) is not int
            or type(high_bound) is not int
            or type(unique_count) is not int):
        raise ArgTypeError("Аргументы должны быть целыми числами")

    if seed is not None and type(seed) is not int:
        raise ArgTypeError("Seed должен быть целым числом")

    if n < 0:
        raise ArgValueError("Размер массива не может быть отрицательным")

    if low_bound > high_bound:
        raise ArgValueError("Нижняя граница больше верхней")

    if unique_count < 1:
        raise ArgValueError("Количество различных значений должно быть положительным")

    if n == 0:
        return []

    rng = random.Random(seed)

    count = min(unique_count, n, high_bound - low_bound + 1)
    values = rng.sample(range(low_bound, high_bound + 1), count)

    return rng.choices(values, k=n)
