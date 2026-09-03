# Movies Quick Sort

## Description

This project contains a Python script that implements the **Quick Sort algorithm** to sort a collection of movies. Quick Sort is a highly efficient, divide-and-conquer sorting algorithm used here to organize movie data .

## Algorithm

The script uses a recursive Quick Sort function to sort the dataset. The step-by-step algorithm is as follows:

1. **Base Case:** Check the length of the list. If the list has fewer than 2 elements (0 or 1), it is already sorted, so return the list as is.
2. **Choose a Pivot:** Select an element from the list to act as the pivot. (This is commonly chosen as the first element, the last element, or a random element in the list).
3. **Partitioning:** Create two new empty sub-lists:
   * **Left Sub-list:** Iterate through the remaining movies and place all items smaller than or equal to the pivot into this list.
   * **Right Sub-list:** Place all items greater than the pivot into this list.
4. **Recursive Sort:** Recursively apply the Quick Sort algorithm to both the Left Sub-list and the Right Sub-list.
5. **Combine:** Concatenate the sorted Left Sub-list, the pivot itself, and the sorted Right Sub-list to form the final, fully sorted list of movies.
6. **Return:** Return the combined sorted list.



## Input and Output

### Input
movies = [
    ("Inception", 8.8),
    ("Interstellar", 8.6),
    ("Titanic", 7.9),
    ("Avatar", 7.8),
    ("The Dark Knight", 9.0)
]


--- Top Rated Movies First ---


The Dark Knight : 9.0


Inception : 8.8


Interstellar : 8.6


Titanic : 7.9


Avatar : 7.8
