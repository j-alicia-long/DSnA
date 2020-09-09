# Algorithms
Mostly written in Python

## Searches
### Breadth-First Search
### Depth-First Search
### Binary Search

## Sorts
Here are some examples of each group of sorting
### Exchange sorting
|     Sort     |  Best      |  Avg       |  Worst  |  Space (Worst) |
|--------------|------------|------------|---------|----------------|
|  Bubble Sort |  O(n)      |  O(n^2)    |  O(n^2) |  O(1)          |
|  Quick Sort  |  O(n logn) |  O(n logn) |  O(n^2) |  O(logn)       |

### Selection Sorting

|     Sort       |  Best      |  Avg       |  Worst     |  Space |
|----------------|------------|------------|------------|--------|
| Selection Sort |  O(n^2)    |  O(n^2)    |  O(n^2)    |  O(1) |
|  Heap Sort     |  O(n logn) |  O(n logn) |  O(n logn) |  O(1) |

Note: Selection sort needs n(n-1)/2 total comparisons (total pairs), thus cannot surpass O(n^2)

### Insertion Sorting
|     Sort        |  Best      |  Avg       |  Worst  |  Space (Worst) |
|-----------------|------------|------------|---------|----------------|
|  Insertion Sort |  O(n)      |  O(n^2)    |  O(n^2) |  O(1) |
|  Merge Sort     |  O(n logn) |  O(n logn) |  O(n^2) |  O(n) |
|  Timsort        |  O(n)      |  O(n logn) |  O(n^2) |  O(n) |
Note: Timsort is used natively in python's sort().

### Stable sorts
- Bubble sort
- Insertion sort
- Merge sort
- Counting Sort
- Radix Sort
These sorts maintain the relative order of the input list.

### Linear Sorts
Sorts that don't use comparisons. Can sort in linear time under specific conditions of input data.
- Bucket Sort, Counting Sort, Radix Sort


## Dynamic Programming
Trading time for space, by storing values to avoid repeated work.
- DP problems must have optimal substructure

### Top-Down Approach (Recursive with Memoization)

Note:
- For memoization in python, use the [@lru_cache()](https://www.geeksforgeeks.org/python-functools-lru_cache/) tag on a function to store most recent function calls

### Bottom-up Approach (Iterative)
A little trickier to come up with, but can save time & space.


## Backtracking
Similar to DFS but with the additional steps of backtracking
