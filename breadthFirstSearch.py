from collections import deque

def breadthFirstSearch(graph, start, search_key):
        # create queue
        search_queue = deque()

        # get startng node
        search_queue += graph[start]

        # while queue is not empty
        while search_queue:

                # dequeue node
                node = search_queue.popleft()

                # check search condition here
                if (node == search_key):
                        return True
                else:
                        # if not found, enqueue the node's neighbours
                        search_queue += graph[node]
        # not found
        return False


