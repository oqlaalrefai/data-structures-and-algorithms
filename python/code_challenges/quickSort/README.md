# Challenge Summary
<!-- Description of the challenge -->
QuickSort selects a pivot element and splits the elements of an array into two new arrays. Numbers higher than the pivot go into one array; numbers lower than the pivot go into another. Each array is sorted and then all the arrays are merged into one
## Whiteboard Process
<!-- Embedded whiteboard image -->
![Quick sort](Quicksort.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
iteration using loop

- Space complexity : O(log(n))
- Time complexity : O(n^2)
## Solution
<!-- Show how to run your code, and examples of it in action -->
Code :
`print(QuickSort([54,26,93,17,77,31,44,55,20], 0, 8))`
Output:
`[17, 20, 26, 31, 44, 54, 55, 77, 93]`