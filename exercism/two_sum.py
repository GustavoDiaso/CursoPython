def two_sum_unsorted(arr, target):
    seen = set()

    for num in arr:
        diff = target - num
        if diff in seen:
            return (diff, num)  # Encontrou o par
        seen.add(num)

    return None  # Nenhum par encontrado


print(
    two_sum_unsorted([1, 3, 7, 10, 5, 9, 12], 9)
)  # Output: (3, 6) não existe, então None

print(two_sum_unsorted([1, 3, 7, 10, 5, 9, 12], 10))  # Output: (3, 7)
