def snail(array):
    result = []
    while array:
        # Take the first row
        result += array.pop(0)
        # Take the last element of each remaining row
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        # Take the last row in reverse order
        if array:
            result += array.pop()[::-1]
        # Take the first element of each remaining row (in reverse order)
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result


# Example usage:
array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(snail(array1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

array1 = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]
print(snail(array1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

array1 = ([[1, 2, 3]])
print(snail(array1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

array1 = ([[1],
           [2],
           [3]])
print(snail(array1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
