from collections import deque

def binarySearch(inputList, item):
        return None

def quicksort(array):
        return array

def breadthFirstSearch(graph, start, search_key):
        search_queue = deque()
        visited = []
        search_queue += graph[start]

        while search_queue:
                vertex = search_queue.popleft()
                if vertex not in visited:
                        if (vertex == search_key):
                                return True
                        else:
                                search_queue += graph[vertex]
                                visited.append(vertex)
        return False
