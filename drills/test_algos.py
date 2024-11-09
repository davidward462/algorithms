import pytest
import algos as a

def test_binarySearch():
        assert a.binarySearch([], 1) == None
        assert a.binarySearch([1], 1) == 0
        assert a.binarySearch([1, 2], 3) == None
        assert a.binarySearch([1, 2], 1) == 0
        assert a.binarySearch([1, 2, 3], 3) == 2

