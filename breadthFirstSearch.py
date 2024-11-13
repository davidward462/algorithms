from collections import deque

def breadthFirstSearch(graph, start, search_key):
        # create queue
        search_queue = deque()
        visited = []

        # get startng node
        search_queue += graph[start]

        # while queue is not empty
        while search_queue:

                # dequeue node
                node = search_queue.popleft()
                print(node)

                # if node has not been visited
                if node not in visited:

                        # check search condition here
                        if (node == search_key):
                                return True
                        else:
                                # if not found, enqueue the node's neighbours
                                search_queue += graph[node]
                                visited.append(node)
        # not found
        return False


