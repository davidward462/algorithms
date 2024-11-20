import dijkstra as djk
def do_bfs():
        graph = {}
        graph = {}
        graph["you"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []

        return

def do_dijkstra():

        # graph
        graph = {}
        graph["start"] = {}
        graph["start"]["a"] = 6
        graph["start"]["b"] = 2
        graph["a"] = {}
        graph["a"]["end"] = 1
        graph["b"] = {}
        graph["b"]["a"] = 3
        graph["b"]["end"] = 5
        graph["end"] = {}

        # costs
        infinity = float("inf")
        costs = {}
        costs["a"] = 6
        costs["b"] = 2
        costs["end"] = infinity

        # parents
        parents = {}
        parents["a"] = "start"
        parents["b"] = "start"
        parents["end"] = None

        djk.dijkstra(graph, costs, parents)
        solution = djk.path(parents, "start", "end")
        return solution

def main():
        do_bfs()
        print(do_dijkstra())

main()
