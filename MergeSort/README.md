 C. Divide and Conquer

## 1. Large Student Dataset

### Question

You have **1 crore (10 million) student records** and need to sort them efficiently.

**How can the Divide-and-Conquer strategy be applied? Identify the divide, conquer, and combine steps.**

---

## Solution

According to the scenario, **Merge Sort** can be used to sort 1 crore student records efficiently. Merge Sort follows the **Divide-and-Conquer** approach.

### Example

Imagine a college has a large number of student records, and we want to sort the records according to **Student ID**.

**Student IDs:**

```text
105, 102, 108, 101, 106, 103, 107, 104
````

Suppose we want to sort the student IDs in **ascending order**.

---

## 1. Divide

Divide the array into two halves.

```text
105, 102, 108, 101   |   106, 103, 107, 104
```

Divide again:

```text
105, 102   |   108, 101   |   106, 103   |   107, 104
```

Continue dividing until each part contains one element:

```text
105 | 102 | 108 | 101 | 106 | 103 | 107 | 104
```

---

## 2. Conquer

Sort each smaller part.

```text
105, 102  →  102, 105

108, 101  →  101, 108

106, 103  →  103, 106

107, 104  →  104, 107
```

Now sort the larger groups:

```text
102, 105 + 101, 108
        ↓
101, 102, 105, 108
```

```text
103, 106 + 104, 107
        ↓
103, 104, 106, 107
```

---

## 3. Combine

Merge the two sorted halves.

```text
101, 102, 105, 108
          +
103, 104, 106, 107
          ↓
101, 102, 103, 104, 105, 106, 107, 108
```

Therefore, the final sorted student IDs are:

```text
101, 102, 103, 104, 105, 106, 107, 108
```

---

# Algorithm

### Input

* Array `arr` containing student records
* Student ID used as the sorting key

### Steps

1. If the array contains one or zero records, return it.
2. Find the middle position of the array.
3. Divide the array into two halves.
4. Recursively sort the left half.
5. Recursively sort the right half.
6. Merge the two sorted halves.
7. Return the final sorted array.

---

# Python Implementation

```python
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
```

---

# Input

```text
105, 102, 108, 101, 106, 103, 107, 104
```

# Output

```text
Sorted Student IDs: [101, 102, 103, 104, 105, 106, 107, 108]
```

---

# Time Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n log n)      |
| Average Case | O(n log n)      |
| Worst Case   | O(n log n)      |

### Space Complexity

```text
O(n)
```

---

# Divide, Conquer and Combine

| Step        | Description                                                |
| ----------- | ---------------------------------------------------------- |
| **Divide**  | Split 1 crore student records into smaller halves          |
| **Conquer** | Recursively sort each smaller half                         |
| **Combine** | Merge the sorted halves into one completely sorted dataset |

---

# Conclusion

**Merge Sort** is suitable for sorting **1 crore (10 million) student records** because it consistently provides **O(n log n)** time complexity.

It follows the three main steps of the Divide-and-Conquer strategy:

1. **Divide** – Split the large dataset into smaller parts.
2. **Conquer** – Sort each smaller part recursively.
3. **Combine** – Merge the sorted parts to obtain the final sorted dataset.

```
```
