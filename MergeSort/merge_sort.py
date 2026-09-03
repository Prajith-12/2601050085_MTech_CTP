def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # Conquer
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


student_ids = [105, 102, 108, 101, 106, 103, 107, 104]

result = merge_sort(student_ids)

print("Sorted Student IDs:", result)
