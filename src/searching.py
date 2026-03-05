#Note: code generated with ChatGPT

import math

# 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. Binary Search (iterative)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 3. Jump Search
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


# 4. Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + int(
            ((float(high - low) /
              (arr[high] - arr[low])) *
             (target - arr[low]))
        )

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# 5. Exponential Search
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr[:min(i, n)], target)