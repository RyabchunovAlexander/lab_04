from algopack.gcd import gcd_iterative, gcd_recursive
from algopack.generators import (
    generate_almost_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
    generate_with_duplicates,
)
from algopack.heap_sort import heap_sort
from algopack.priority_queue import PriorityQueue
from algopack.selection_sort import selection_sort


def demo_gcd():
    """Демонстрация алгоритма Евклида."""
    a, b = 1071, 462

    print("\n1. Алгоритм Евклида")
    print(f"Числа: {a} и {b}")
    print("Итеративный НОД:", gcd_iterative(a, b))
    print("Рекурсивный НОД:", gcd_recursive(a, b))


def demo_sorts():
    """Демонстрация двух сортировок."""
    numbers = [8, -3, 5, 1, 8, 0]

    print("\n2. Сортировки")
    print("Исходный список:", numbers)
    print("Selection Sort:", selection_sort(numbers))
    print("Heap Sort:", heap_sort(numbers))
    print("Исходный список после сортировок:", numbers)


def demo_queue():
    """Демонстрация очереди с приоритетом."""
    queue = PriorityQueue()

    queue.push("Обычная задача", 2)
    queue.push("Срочная задача", 10)
    queue.push("Проверка", 5)

    print("\n3. Очередь с приоритетом")
    print("Количество элементов:", len(queue))
    print("Следующий элемент:", queue.peek())

    while queue:
        print("Извлечён:", queue.pop())

    print("Очередь пуста:", not queue)


def demo_generators():
    """Демонстрация генераторов тестовых наборов."""
    n = 10
    seed = 42

    print("\n4. Генераторы массивов")
    print("Случайный:", generate_random(n, seed))
    print("Отсортированный:", generate_sorted(n, seed))
    print("Обратный:", generate_reversed(n, seed))
    print("Почти отсортированный:", generate_almost_sorted(n, seed))
    print("С повторениями:", generate_with_duplicates(n, seed))


def main():
    """Главная функция демонстрации лабораторной."""
    print("=" * 50)
    print("Лабораторная работа №4")
    print("Алгоритмический мини-пакет")
    print("=" * 50)

    demo_gcd()
    demo_sorts()
    demo_queue()
    demo_generators()

    print("\nДемонстрация завершена.")


if __name__ == "__main__":
    main()
