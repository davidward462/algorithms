import pytest
import binarySearch as bs
import selectionSort as ss
import recursion as r
import quicksort as qs
import breadthFirstSearch as bfs
import dijkstra as djk

def test_binarySearch():
        assert bs.binarySearch([1, 2, 3, 4, 6, 29, 100], 100) == 6
        assert bs.binarySearch([23], 23) == 0
        assert bs.binarySearch([-3, 0, 3, 6, 9, 10, 12, 50, 55, 69], 3) == 2
        assert bs.binarySearch([2, 6, 10], 23) == None


def test_findSmallest():
        assert ss.findSmallest([2, 6, 1, 9]) == 2
        assert ss.findSmallest([0]) == 0
        assert ss.findSmallest([9, 3, 10, 7, 6, 4, 5]) == 1


def test_selectionSort():
        assert ss.selectionSort([10]) == [10]
        assert ss.selectionSort([2, 56]) == [2, 56]
        assert ss.selectionSort([9, 2, 3, 10, 7]) == [2, 3, 7, 9, 10]

def test_recursion():
        assert r.fact(1) == 1
        assert r.fact(3) == 6
        assert r.fact(5) == 120

def test_sum():
        assert r.sum([1, 2, 0, 10]) == 13
        assert r.sum([37]) == 37
        assert r.sum([-1, 0, 0, 1, 100, -40]) == 60

def test_quicksort():
        assert qs.quicksort([1]) == [1]
        assert qs.quicksort([]) == []
        assert qs.quicksort([1, 3, 2]) == [1, 2, 3]
        assert qs.quicksort([10, 2, 9, 3, 8, 5, 4, 7, 6, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_bfsEmpty():
        graph = {}
        graph["start"] = []
        assert bfs.breadthFirstSearch(graph, "start", "end") == False

def test_bfs():
        graph = {}
        graph["start"] = ["A", "B", "C"]
        graph["A"] = ["start", "D"]
        graph["B"] = ["start"]
        graph["C"] = ["start", "F", "G", "H"]
        graph["D"] = ["A", "E"]
        graph["E"] = ["D"]
        graph["F"] = ["C"]
        graph["G"] = ["C"]
        graph["H"] = ["C"]
        assert bfs.breadthFirstSearch(graph, "start", "A") == True
        assert bfs.breadthFirstSearch(graph, "start", "B") == True
        assert bfs.breadthFirstSearch(graph, "start", "X") == False
        assert bfs.breadthFirstSearch(graph, "start", "G") == True
        assert bfs.breadthFirstSearch(graph, "H", "A") == True

def test_dijkstra_A():
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
        path = djk.get_path(parents, "start", "end")
        weight = costs["end"]

        assert weight == 6
        assert path == ["start", "b", "a", "end"]

def test_dijkstra_B():
        # graph
        graph = {}
        graph["start"] = {}
        graph["A"] = {}
        graph["B"] = {}
        graph["C"] = {}
        graph["D"] = {}
        graph["end"] = {}
        graph["start"]["A"] = 5
        graph["start"]["B"] = 2
        graph["A"]["C"] = 4
        graph["A"]["D"] = 2
        graph["B"]["A"] = 8
        graph["B"]["D"] = 7
        graph["C"]["end"] = 3
        graph["C"]["D"] = 6
        graph["D"]["end"] = 1

        # costs
        infinity = float("inf")
        costs = {}
        costs["A"] = 5
        costs["B"] = 2
        costs["C"] = infinity
        costs["D"] = infinity
        costs["end"] = infinity

        # parents
        parents = {}
        parents["A"] = "start"
        parents["B"] = "start"
        parents["C"] = None
        parents["D"] = None
        parents["end"] = None

        djk.dijkstra(graph, costs, parents)
        path = djk.get_path(parents, "start", "end")
        weight = costs["end"]

        assert weight == 8
        assert path == ["start", "A", "D", "end"]



