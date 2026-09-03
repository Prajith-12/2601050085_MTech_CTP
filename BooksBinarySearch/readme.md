# Books Binary Search

## Description

This project contains a Python script that implements the **Binary Search algorithm** to find a specific book in a virtual library. The library is represented by a list of numbers ranging from **1 to 1,000,000**.

## Algorithm

The script uses a `Library(target)` function to locate the book efficiently. The step-by-step algorithm is as follows:

1. **Initialize Boundaries:** Set a `low` pointer to the first index (0) and a `high` pointer to the last index of the list.
2. **Iterate:** While the `low` pointer is less than or equal to the `high` pointer, repeat the following steps:
   * **Find Midpoint:** Calculate the middle index, `mid`, by finding the average of `low` and `high`.
   * **Check Match:** Compare the value at `mid` with the target book. If they match, return the `mid` index.
   * **Search Left:** If the target is smaller than the value at `mid`, the book must be in the left half. Update the `high` pointer to `mid - 1`.
   * **Search Right:** If the target is larger than the value at `mid`, the book must be in the right half. Update the `low` pointer to `mid + 1`.
3. **Not Found:** If the loop concludes without finding the target, return `-1` to indicate the book is not in the library.




## Input and Output

### Input
What book do you want to find: 7500

### Output
Book at: 7499
