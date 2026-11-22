import csv
import time
from pathlib import Path

from algopack.generators import (
    generate_almost_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
    generate_with_duplicates,
)
from algopack.heap_sort import heap_sort
from algopack.selection_sort import selection_sort


def measure_time(sort_func, data):
    """Измеряет время сортировки в миллисекундах."""
    expected = sorted(data)
    numbers = data.copy()

    start = time.perf_counter()
    result = sort_func(numbers)
    end = time.perf_counter()

    if result != expected:
        raise AssertionError("Сортировка вернула неправильный результат")

    if numbers != data:
        raise AssertionError("Сортировка изменила переданный список")

    return (end - start) * 1000


def save_report(results, measurements):
    """Сохраняет итоговую таблицу и отдельные измерения."""
    folder = Path(__file__).resolve().parents[2]

    with open(folder / "benchmark.csv", "w",
              newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Алгоритм",
            "Тип массива",
            "Размер",
            "Повторы",
            "Среднее время (мс)",
            "Минимальное время (мс)",
            "Максимальное время (мс)",
            "Рост времени"
        ])

        writer.writerows(results)

    with open(folder / "benchmark_runs.csv", "w",
              newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Алгоритм",
            "Тип массива",
            "Размер",
            "Номер повтора",
            "Seed",
            "Время (мс)"
        ])

        writer.writerows(measurements)


def run_benchmarks():
    """Запускает измерение производительности сортировок."""
    algorithms = {
        "Selection Sort": (selection_sort, [100, 1000, 10000]),
        "Heap Sort": (heap_sort, [
            100, 1000, 10000, 100000, 1000000, 10000000
        ])
    }

    generators = {
        "Случайный": generate_random,
        "Отсортированный": generate_sorted,
        "Обратный": generate_reversed,
        "Почти отсорт.": generate_almost_sorted,
        "С повторениями": generate_with_duplicates
    }

    repeats = 5
    results = []
    measurements = []

    for algorithm_name, (sort_func, sizes) in algorithms.items():
        print("\n" + "=" * 83)
        print(f"{algorithm_name:^83}")
        print("=" * 83)

        print(
            f"{'Тип массива':<20} {'Размер':>12} "
            f"{'Среднее, мс':>15} {'Мин, мс':>12} "
            f"{'Макс, мс':>12} {'Рост':>8}"
        )
        print("-" * 83)

        for kind_index, (kind, generator) in enumerate(generators.items()):
            previous_time = None

            for n in sizes:
                times = []

                for repeat in range(1, repeats + 1):
                    seed = (kind_index + 1) * 1000000000 + n * 10 + repeat

                    data = generator(n, seed=seed)
                    elapsed = measure_time(sort_func, data)

                    times.append(elapsed)
                    measurements.append([
                        algorithm_name, kind, n,
                        repeat, seed, elapsed
                    ])

                    del data

                average = sum(times) / repeats
                minimum = min(times)
                maximum = max(times)

                if previous_time is None or previous_time == 0:
                    growth = "-"
                else:
                    growth = f"{average / previous_time:.2f}x"

                size_text = f"{n:,}".replace(",", " ")

                print(
                    f"{kind:<20} {size_text:>12} "
                    f"{average:>15.3f} {minimum:>12.3f} "
                    f"{maximum:>12.3f} {growth:>8}",
                    flush=True
                )

                results.append([
                    algorithm_name,
                    kind,
                    n,
                    repeats,
                    round(average, 3),
                    round(minimum, 3),
                    round(maximum, 3),
                    growth
                ])

                save_report(results, measurements)
                previous_time = average

            print("-" * 83)

    print("\nВсе измерения завершены.")
    print("Selection Sort: O(n^2)")
    print("Heap Sort: O(n log n)")
    print("Результаты сохранены в benchmark.csv и benchmark_runs.csv")


if __name__ == "__main__":
    run_benchmarks()
