# Python Info

## Is Python pass-by-reference?
Yes, Python is pass by reference in all cases. The key point is that some objects are immutable and cannot be changed (ex. numeric types, strings, tuples). When we attempt to mutate them, a new object reference (with the updated value) is assigned to the variable instead. This is sometimes called **pass-by-assignment**.

Note: Python does not actually have traditional primitive types - they are all objects.

Source:
- https://www.quora.com/How-do-I-pass-a-variable-by-reference-in-Python/answer/Tony-Flury


## Time complexities of built-in python data structures
Source:
- https://wiki.python.org/moin/TimeComplexity


## What algorithm does Python 3's sort() use?
**Timsort** - O(n) Best, O(n logn) Avg/Worst
- Hybrid algorithm derived from Merge Sort and insertion sort
- Idea: Finds already-ordered subsets of data, and uses them to sort more efficiently

Performance
- Implemented in hand-optimized C
- Designed to perform well on real-world data
- Stable, not parallelizable, not in-place, adaptive
