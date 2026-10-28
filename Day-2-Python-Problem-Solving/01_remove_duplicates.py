def unique_in_order(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


print(unique_in_order([]))
print(unique_in_order([5]))
print(unique_in_order([2, 2, 2]))
print(unique_in_order([3, 1, 3, 2, 1]))
print(unique_in_order([4, 2, 4, 1, 2]))