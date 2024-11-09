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

## Breadth-First Search
- graph algorithm
- determine the number of paths from node A to B
- determine the length of a path from node A to B
- For each connected node N, search N and then append all of N's neighbours to the list of nodes to search
- All first degree connections are searched before second degree connections, and so on

# Data Structures

## Array
- contiguous memory
- random access
- read: O(1)
- insert: O(n) because of worst case where you need to move all the values to a new part of memory if it's full
- delete: O(n)

## Linked List
- not contiguous memory
- sequential access
- read: O(n)
- insert: O(1)
- delete: O(1)

## Hash Table (Map)
- Array and hash function h(x)
- Input data into h(x) and get an index
- read: O(1)
- insert:
    - best/average: O(1)
    - worse: O(n) where either all elements are hashing to the same value, or the array is full
- delete:
    - best/average: O(1)
    - worst: O(n)
- Collision reduction:
    - keep load factor low
        - items in table per total number of array slots
        - resize at load factor > ~0.7
    - use a good hash function
- Collision resolution:
    - open addressing: look for an open spot in the subsequent slots of the array
    - separate chaining: Each slot of the array is also a linked list to hold several values

## Graph
- a set of nodes and edges

# Techniques

## Divide and Conquer
- recursive
1. Determine a simple base case
2. Divide or decrease the problem until you reach the base case
