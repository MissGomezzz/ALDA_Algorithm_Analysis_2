# Note: code generated with ChatGPT

import math


# 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):                 # loop may scan the entire array -> O(n)
        if arr[i] == target:                  # constant comparison -> O(1)
            return i
    return -1                                 # if not found after checking all elements -> still O(n)


# 2. Binary Search (iterative)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:                      # each iteration halves the search space -> O(log n)
        mid = (left + right) // 2             # constant calculation -> O(1)

        if arr[mid] == target:                # constant comparison -> O(1)
            return mid
        elif arr[mid] < target:
            left = mid + 1                    # discard left half of array -> logarithmic reduction
        else:
            right = mid - 1                   # discard right half of array -> logarithmic reduction

    return -1


# 3. Jump Search
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))                  # jump size is sqrt(n) -> leads to O(sqrt(n)) complexity
    prev = 0

    while arr[min(step, n) - 1] < target:     # jumping through blocks of size sqrt(n)
        prev = step
        step += int(math.sqrt(n))             # number of jumps is about sqrt(n) -> O(sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):       # linear search inside the block -> O(sqrt(n))
        if arr[i] == target:
            return i

    return -1                                 # overall complexity: sqrt(n) jumps + sqrt(n) scan -> O(sqrt(n))


# 4. Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:   # search space shrinks based on value estimation
    
    # average case reduces search dramatically -> O(log log n)

        if low == high:                                     # constant check -> O(1)
            if arr[low] == target:
                return low
            return -1

        pos = low + int(
            ((float(high - low) /
              (arr[high] - arr[low])) *                     # interpolation formula predicts likely position
             (target - arr[low]))                           # good prediction reduces steps significantly
        )

        if arr[pos] == target:                              # constant comparison -> O(1)
            return pos

        if arr[pos] < target:
            low = pos + 1                                   # discard lower part -> reduces search range
        else:
            high = pos - 1                                  # discard upper part -> reduces search range

    return -1                                               # average case O(log log n), worst case O(n)


# 5. Exponential Search
def exponential_search(arr, target):
    if arr[0] == target:                # constant check -> O(1)
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:   # index grows exponentially (1,2,4,8,16...) -> O(log n)
        i *= 2                          # doubling step quickly finds a range containing target

    return binary_search(arr[:min(i, n)], target)  # binary search on reduced range -> O(log n)

# total complexity dominated by logarithmic steps