# Program 10: Sequential Processing vs Parallel Processing

from multiprocessing import Pool
from time import perf_counter

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers = list(range(1, 5_000_001))

    # Sequential processing
    start = perf_counter()
    sequential_sum = calculate_sum(numbers)
    sequential_time = perf_counter() - start

    # Parallel processing
    workers = 4
    chunk_size = len(numbers) // workers

    chunks = [
        numbers[i * chunk_size:(i + 1) * chunk_size]
        for i in range(workers - 1)
    ]
    chunks.append(numbers[(workers - 1) * chunk_size:])

    start = perf_counter()
    with Pool(processes=workers) as pool:
        partial_sums = pool.map(calculate_sum, chunks)

    parallel_sum = sum(partial_sums)
    parallel_time = perf_counter() - start

    print("Sequential sum:", sequential_sum)
    print("Parallel sum  :", parallel_sum)
    print(f"Sequential time: {sequential_time:.4f} seconds")
    print(f"Parallel time  : {parallel_time:.4f} seconds")
    print("Results match  :", sequential_sum == parallel_sum)