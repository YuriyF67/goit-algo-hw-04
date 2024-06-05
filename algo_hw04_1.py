import random
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def timsort(arr):
    return sorted(arr)


def generate_test_data(size):
    random_data = [random.randint(0, size) for _ in range(size)]
    sorted_data = sorted(random_data)
    reversed_data = sorted(random_data, reverse=True)
    return random_data, sorted_data, reversed_data


def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data.copy()), number=1)


sizes = [1000, 5000, 10000, 20000]

for size in sizes:
    random_data, sorted_data, reversed_data = generate_test_data(size)

    print(f"\nTesting with array size: {size}")

    merge_sort_time = measure_time(merge_sort, random_data)
    print(f"Merge Sort Time (random): {merge_sort_time} seconds")

    insertion_sort_time = measure_time(insertion_sort, random_data)
    print(f"Insertion Sort Time (random): {insertion_sort_time} seconds")

    timsort_time = measure_time(timsort, random_data)
    print(f"Timsort Time (random): {timsort_time} seconds")
