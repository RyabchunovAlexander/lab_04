from algopack.errors import ArgTypeError, EmptyQueueError


class PriorityQueue:
    """Очередь с приоритетом на основе отсортированного списка."""

    def __init__(self):
        self.elements = []

    def push(self, value, priority):
        """Добавление элемента в очередь."""
        if type(priority) is not int:
            raise ArgTypeError("Приоритет должен быть целым числом")

        self.elements.append((priority, value))

        for i in range(len(self.elements) - 1, 0, -1):
            if self.elements[i][0] <= self.elements[i - 1][0]:
                self.elements[i], self.elements[i - 1] = (
                    self.elements[i - 1], self.elements[i]
                )
            else:
                break

    def pop(self):
        """Извлечение элемента с наибольшим приоритетом."""
        if not self.elements:
            raise EmptyQueueError("Очередь пуста")

        return self.elements.pop()[1]

    def peek(self):
        """Просмотр элемента с наибольшим приоритетом."""
        if not self.elements:
            raise EmptyQueueError("Очередь пуста")

        return self.elements[-1][1]

    def __len__(self):
        """Возвращает количество элементов."""
        return len(self.elements)

    def __bool__(self):
        """Проверяет наличие элементов в очереди."""
        return bool(self.elements)
