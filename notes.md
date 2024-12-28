# Algorithms

## Binary Search
- Runtime: O(log n)
- Input array must be sorted

## Quicksort
- Uses Divide and Conquer
- Base case and recursive case
- Worst case: O(n^2)
- Average case (choose random pivot): O(n log n)
1. An array with one or zero items is already sorted (base case)
2. Choose a pivot (random index is good)
3. Partition the array into two subarrays: one of values less than the pivot, one of values greater than it
4. Call quicksort recursively on the two subarrays

## Breadth-First Search
- Graph algorithm
- Determine the number of paths from node A to B
- Determine the length of a path from node A to B
- Unweighted graph
- For each node N to visit, visit N and then append all of N's neighbours to the list of nodes to visit
- All first degree connections are searched before second degree connections, and so on
- Traverse graph: O(V + E) where V is the number of nodes or verticies, and E is the number of edges

## Dijkstra's Algorithm
- Find the shortest path in a graph from node A to node B
- Each edge in the path has a weight (weighted graph)
- Only works for directed acyclic graphs, without negative edge weights
- Basic steps:
    1. Find the cheapest node, the one which can be arrived at in the least amount of time
    2. Check if there is a cheaper path to the neighbours of this node. If so, update their costs
    3. Repeat until this has been done for every node
    4. Calculate the final path
- Uses three hash tables:
    1. the graph (with hash table for each node to store the weights of the node's edges)
    2. the node costs
    3. the parents to each node
- There is an array which keeps track of the nodes that have been processed

## K-Nearest Neighbours

# Data Structures

## Array
- Contiguous memory
- Random access
- Read: O(1)
- Insert: O(n) because of worst case where you need to move all the values to a new part of memory if it's full
- Delete: O(n)

## Linked List
- Not contiguous memory
- Sequential access of data
- Head and tail pointers
- Read: O(n)
- Insert: O(1)
- Delete: O(1)

## Hash Table (Map)
- Array and hash function h(x)
- Input data into h(x) and get an index
- Read: O(1)
- Insert:
    - best/average: O(1)
    - worse: O(n) where either all elements are hashing to the same value, or the array is full
- Delete:
    - best/average: O(1)
    - worst: O(n)
- Collision reduction:
    - keep load factor low
        - load factor = items in talbe / total number of array slots
        - resize when load factor > ~0.7
    - use a good hash function
- Collision resolution:
    - open addressing: look for an open spot in the subsequent slots of the array
    - separate chaining: Each slot of the array is also a linked list to hold several values

## Stack
- Sequential
- Has operations push and pop
- Last In, First Out
- Push and Pop: O(1)

## Queue
- Sequential
- Has operations enqueue and dequeue
- First In, First Out
- Enqueue and dequeue: O(1)

## Graph
- A set of nodes and edges
- Directed vs nondirected graph
- Implementation
    - Hash table relationships between nodes

# Techniques and Problem Types
## Divide and Conquer
- Recursive
1. Determine a simple base case
2. Divide or decrease the problem until you reach the base case

## Greedy Algorithms
- For problems with no general optimal solution
- At each step, choose the locally optimal decision
- A greedy algorithm may generate a globally optimal solution
- Examples:
    - Classroom scheduling (has a globally optimal solution)
        1. Choose the class which ends the soonest
        2. Of the remaining classes which do not conflict, choose the one the ends soonest
- Greedy algorithms can also be used as approximation algorithms for NP-complete problems (which have no fast solution). For example:
    - Traveling Salesman
    - Set-covering problem

## Dynamic Programming
- Optimizing values given some a constraint
- Problem is broken up into discrete subproblems that do not depend on one another
- Solve the sub-problems, which eventually result in solving the full problem
- Example:
    - Knapsack problem
    - Longest common substring
- solution uses a grid of cells to keep track of sub-problems and corresponding solutions
    - each cell is a subproblem
    - the values in the cell are are usually what we are trying to optimize
### Longest Common Substring and Subsequence
- Subsequence: any characters which are matching
    - if letters are equal, set cell to grid[i-1][j-1] + 1
    - if letters are different, set cell to max(grid[i-1][j], grid[i][j-1])
- Substring: contiguous set of characters which are matching
    - if letters are equal, set cell to grid[i-1][j-1] + 1
    - if letters are different, set cell to 0 
- Number in the cells are the length of the string or sequence we are measuring
- Answer is the largest value in the grid

## NP-Complete (Non-polynomial time)
- There is no fast perfect solution (would take exponential or factorial time)
- Examples:
    - Traveling Salesman
    - Set-covering problem
- Traits:
    - Runs fast with a small number of items but slows down significantly as the number increases
    - "All combinations of..."
    - You need to calculate "every possible version" of something
    - The problem can be translated into either the traveling salesman or set-covering problems
- The solution must be approximated (like with a greedy algorithm or something else)
