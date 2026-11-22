class AlgoPackError(Exception):
    """Базовый класс ошибок пакета."""


class ArgTypeError(AlgoPackError, TypeError):
    """Неверный тип аргумента."""


class ArgValueError(AlgoPackError, ValueError):
    """Недопустимое значение аргумента."""


class GCDError(ArgValueError):
    """НОД двух нулей не определён."""


class EmptyQueueError(AlgoPackError, IndexError):
    """Операция над пустой очередью."""
