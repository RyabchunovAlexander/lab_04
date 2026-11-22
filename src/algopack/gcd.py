from algopack.errors import ArgTypeError, GCDError


def gcd_iterative(a, b):
    """Итеративный алгоритм Евклида."""
    if type(a) is not int or type(b) is not int:
        raise ArgTypeError("Аргументы должны быть целыми числами")

    if a == 0 and b == 0:
        raise GCDError("НОД(0, 0) не определён")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def gcd_recursive(a, b):
    """Рекурсивный алгоритм Евклида."""
    if type(a) is not int or type(b) is not int:
        raise ArgTypeError("Аргументы должны быть целыми числами")

    if a == 0 and b == 0:
        raise GCDError("НОД(0, 0) не определён")

    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd_recursive(b, a % b)
