from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary Search Algorithm (Divide and Conquer)

    Assumes the input list is sorted.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    data = [1, 3, 4, 6, 8, 10]
    print(binary_search(data, 6))
