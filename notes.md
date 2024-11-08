# Algorithms

## Binary Search

- runtime: O(log n)
- input array must be sorted

## Quicksort
- uses Divide and Conquer
- worst case: O(n^2)
- average case (choose random pivot): O(n log n)
1. An array with one or zero items is already sorted (base case)
2. Choose a pivot
3. Partition the array into two subarrays: one of values less than the pivot, one of values greater than it
4. Call quicksort recursively on the two subarrays

# Data Structures

## Array
- contiguous memory
- random access
- read: O(1)
- insert: O(n) because of worst case where you need to move all the values to a new part of memory if it's full
- delete: O(n)

## Linked list
- not contiguous memory
- sequential access
- read: O(n)
- insert: O(1)
- delete: O(1)

# Techniques

## Divide and Conquer
- recursive
1. Determine a simple base case
2. Divide or decrease the problem until you reach the base case
