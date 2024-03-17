def remove_all_after(numbers, n):
    ...
    if n in numbers:
        return numbers[:numbers.index(n) + 1]
    return numbers
numbers = [1, 1, 2, 2, 3, 3]
n = int(input("n = "))
result = remove_all_after(numbers, n)
print(f"numbers: {result}")

