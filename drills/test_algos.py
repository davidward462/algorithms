import pytest
import algos as a

'''
def test_binarySearch():
        assert a.binarySearch([], 1) == None
        assert a.binarySearch([1], 1) == 0
        assert a.binarySearch([1, 2], 3) == None
        assert a.binarySearch([1, 2], 1) == 0
        assert a.binarySearch([1, 2, 3], 3) == 2
'''

'''
def test_quicksort():
        assert a.quicksort([]) == []
        assert a.quicksort([8]) == [8]
        assert a.quicksort([1, 2]) == [1, 2]
        assert a.quicksort([9, 3]) == [3, 9]
        assert a.quicksort([1, 3, 5]) == [1, 3, 5]
        assert a.quicksort([10, 1, 3]) == [1, 3, 10]
        assert a.quicksort([12, 8, 9, 2, 5, 10, 1, 7]) == [1, 2, 5, 7, 8, 9, 10, 12]
'''

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
        assert a.breadthFirstSearch(graph, "start", "A") == True
        assert a.breadthFirstSearch(graph, "start", "B") == True
        assert a.breadthFirstSearch(graph, "start", "X") == False
        assert a.breadthFirstSearch(graph, "start", "G") == True
        assert a.breadthFirstSearch(graph, "H", "A") == True
