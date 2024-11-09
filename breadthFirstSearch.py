from collections import deque

def breadthFirstSearch(graph, start, search_key):
        search_queue = deque()
        search_queue += graph[start]

        # while queue is not empty
        while search_queue:
                node = search_queue.popleft() #dequeue
                if (node == search_key):
                        return True
                else:
                        search_queue += graph[node]
        # not found
        return False


