# Program 9: Data Parallelism

from multiprocessing import Pool

def find_squares(numbers):
    return [number ** 2 for number in numbers]

if __name__ == "__main__":
    numbers = list(range(1, 11))

    middle = len(numbers) // 2

    parts = [
        numbers[:middle],
        numbers[middle:]
    ]

    with Pool(processes=2) as pool:
        processed_parts = pool.map(find_squares, parts)

    combined_result = [
        value
        for part in processed_parts
        for value in part
    ]

    for worker, (part, processed) in enumerate(
        zip(parts, processed_parts),
        start=1
    ):
        print(
            f"Worker {worker}: "
            f"input={part}, output={processed}"
        )

    print("Combined result:", combined_result)