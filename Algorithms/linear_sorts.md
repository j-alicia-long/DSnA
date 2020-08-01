# Linear Sorts
Linear sorts don't use comparisons to gain information about values. It's possible to use linear sorts under specific conditions - assumptions must be made about the input data.

## Bucket Sort - O(n)
Sort uniformly distributed data into buckets

  BucketSort(A, n):
    Allocate B[0..n-1] empty lists

    for i in 1 .. n loop
        insert A[i] into list B[floor(n * A[i])]

    for i in 0 .. n-1 loop
        sort list B[i] with insertion sort (often O(n))
        OR recursively BucketSort(B[i])

    Concatenate lists B[0..n-1], in order

    Return concatenated lists

Notes:
- Insertion sort is often O(1) due to small avg bucket size
  - if uniformly distributed, could be 1-2 per bucket
- Not efficient for non-uniform data
  - Bucket sizes would be larger


## Counting Sort - O(n+k)
Count the number of objects having distinct key values, then calculate the position of each in the output sequence.

  CountingSort(A, B, n, k)
    # Freq lists with arbitrary large k
    Allocate C(0..k) of Natural := (others => 0)

    # Count frequencies of each number
    for j in 1 .. n loop
        C[A[j]] := C[A[j]] + 1

    # Calculate cumulative counts
    for i in 1 .. k loop
        C[i] := C[i] + C[i-1]

    # Output list
    for j in reverse 1 .. n loop
        B[C[A[j]]] := A[j]
        C[A[j]] := C[A[j]] - 1

Notes:
- Trades time for space
- Not efficient for wide ranges (where range >> input size)
- Must be able to use keys as array indices (no non-int inputs)


## Radix Sort - O(d(n+k))
Sorts by digits, *least significant* first to avoid recursion.

  RadixSort(A, d)  -- To sort d digits
    for i in 1 .. d loop
        use a stable sort to sort A on digit i

Performance:
- n numbers, with digits in range 0 .. k
  - Cost per pass: Θ(n + k)
- each number has d digits, thus d passes
- Total: Θ(d(n + k))

Notes:
- Often uses counting sort as a subroutine within each digit
- Used by IBM Card Sorter
