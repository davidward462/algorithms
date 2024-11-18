def lowest_cost_node(costs, processed):
        lowest_cost = float("inf")
        lowest_node = None
        for n in costs:
                cost = costs[n]
                if cost < lowest_cost and n not in processed:
                        lowest_cost = cost
                        lowest_node = n
        return lowest_node



def dijkstra(graph, costs, parents):
        processed = []

        # find the lowest cost node
        node = lowest_cost_node(costs, processed)

        while node is not None:
                cost = costs[node] # cost of the node
                neighbours = graph[node] # get the neighbours, which is a hash table

                # go through all the neighbours of node n, where keys() returns a list of nodes
                for n in neighbours.keys():
                        new_cost = cost + neighbours[n]
                        if new_cost < costs[n]:
                                costs[n] = new_cost # update cost of this node
                                parents[n] = node # set this node as the parent of n
                processed.append(node) # mark node as processed
                node = lowest_cost_node(costs, processed) # find next node to process
