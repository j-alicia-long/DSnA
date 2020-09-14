# Sorts Pseudocode

## Bubble Sort
```
  procedure bubbleSort( list : array of items )
    loop = list.count;

    for i = 0 to loop-1 do:
      swapped = false

      for j = 0 to loop-1 do:
        /* compare the adjacent elements */
        if list[j] > list[j+1] then
          /* swap them */
          swap( list[j], list[j+1] )
          swapped = true
        end if
      end for

      /*if no number was swapped that means
      array is sorted now, break the loop.*/
      if(not swapped) then
        break
      end if

    end for

  end procedure return list
```

## Selection Sort
```
  procedure selection sort
    list : array of items
    n : size of list

    for i = 1 to n - 1
      /* set current element as minimum*/
      min = i

      /* check the element to be minimum */
      for j = i+1 to n
        if list[j] < list[min] then
          min = j;
        end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i then
        swap list[min] and list[i]
      end if

    end for
  end procedure
```

## Insertion Sort
```
  procedure insertionSort( A : array of items )
    int holePosition
    int valueToInsert

    for i = 1 to length(A) inclusive do:

      /* select value to be inserted */
      valueToInsert = A[i]
      holePosition = i

      /*locate hole position for the element to be inserted */
      while holePosition > 0 and A[holePosition-1] > valueToInsert do:
        A[holePosition] = A[holePosition-1]
        holePosition = holePosition -1
      end while

      /* insert the number at hole position */
      A[holePosition] = valueToInsert

    end for

  end procedure
```

## Merge Sort
```
  procedure mergesort( var a as array )
    if ( n == 1 ) return a

    var l1 as array = a[0] ... a[n/2]
    var l2 as array = a[n/2+1] ... a[n]

    l1 = mergesort( l1 )
    l2 = mergesort( l2 )

    return merge( l1, l2 )
  end procedure


  procedure merge( var a as array, var b as array )

    var c as array

    while ( a and b have elements )
      if ( a[0] > b[0] )
        add b[0] to the end of c
        remove b[0] from b
      else
        add a[0] to the end of c
        remove a[0] from a
      end if
    end while

    while ( a has elements )
      add a[0] to the end of c
      remove a[0] from a
    end while

    while ( b has elements )
      add b[0] to the end of c
      remove b[0] from b
    end while

    return c

  end procedure
```

## Quick Sort
Need to review quicksort and quickselect
```
  procedure quickSort(left, right)
    if right-left <= 0
      return
    else
      pivot = A[right]
      partition = partitionFunc(left, right, pivot)
      quickSort(left, partition-1)
      quickSort(partition+1, right)
    end if
  end procedure

  function partitionFunc(left, right, pivot)
    leftPointer = left
    rightPointer = right - 1

    while True do
      while A[++leftPointer] < pivot do
        //do-nothing
      end while

      while rightPointer > 0 && A[--rightPointer] > pivot do
        //do-nothing
      end while

      if leftPointer >= rightPointer
        break
      else
        swap leftPointer, rightPointer
      end if
    end while

    swap leftPointer, right
    return leftPointer

  end function
```
