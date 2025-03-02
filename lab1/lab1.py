def search_k(k: int, array: list):
    for i in range(n):
        for j in range(n - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    if k >= len(array):
        raise ValueError("k має бути меншим за довжину масиву")
    else:
        return f"element = {array[k-1]}, index = {array.index(array[k-1])}"

array = [15, 7, 22, 9, 36, 2, 42, 18]
n = len(array)

print(search_k(3, array))
