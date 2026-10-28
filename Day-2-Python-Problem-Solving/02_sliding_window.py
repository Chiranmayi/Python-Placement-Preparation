def max_sum_window(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    best = window_sum

    for right in range(k, len(numbers)):
        window_sum += numbers[right] - numbers[right - k]
        best = max(best, window_sum)

    return best


print(max_sum_window([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_sum_window([1, 2, 3, 4], 2))        # 7
print(max_sum_window([-5, -2, -3], 2))        # -5
print(max_sum_window([10, 20], 1))            # 20
print(max_sum_window([1, 2, 3], 0))           # None
print(max_sum_window([1, 2, 3], 4))           # None
print(max_sum_window([], 1))                  # None