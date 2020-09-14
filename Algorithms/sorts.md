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
