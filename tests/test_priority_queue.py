import pytest

from algopack.errors import ArgTypeError, EmptyQueueError
from algopack.priority_queue import PriorityQueue


def test_priority_order():
    queue = PriorityQueue()

    queue.push("Низкий", 1)
    queue.push("Высокий", 10)
    queue.push("Средний", 5)

    assert queue.pop() == "Высокий"
    assert queue.pop() == "Средний"
    assert queue.pop() == "Низкий"


def test_same_priority():
    queue = PriorityQueue()

    queue.push("Первый", 3)
    queue.push("Второй", 3)
    queue.push("Третий", 3)

    assert queue.pop() == "Первый"
    assert queue.pop() == "Второй"
    assert queue.pop() == "Третий"


def test_peek():
    queue = PriorityQueue()
    queue.push("Задача", 7)

    assert queue.peek() == "Задача"
    assert len(queue) == 1


def test_len_and_bool():
    queue = PriorityQueue()

    assert len(queue) == 0
    assert not queue

    queue.push("Тест", 1)

    assert len(queue) == 1
    assert bool(queue)

    queue.pop()
    assert not queue


def test_empty():
    queue = PriorityQueue()

    with pytest.raises(EmptyQueueError):
        queue.pop()

    with pytest.raises(EmptyQueueError):
        queue.peek()


def test_invalid_priority():
    queue = PriorityQueue()

    with pytest.raises(ArgTypeError):
        queue.push("Задача", 1.5)

    with pytest.raises(ArgTypeError):
        queue.push("Задача", True)


def test_invariant():
    queue = PriorityQueue()

    for priority in [5, 1, 7, 3, 7, -2]:
        queue.push("Задача", priority)

        for i in range(len(queue.elements) - 1):
            assert queue.elements[i][0] <= queue.elements[i + 1][0]
