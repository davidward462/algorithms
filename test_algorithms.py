import pytest
import binarySearch as bs

def test_binarySearch():
        assert bs.binarySearch([1, 2, 3, 4, 6, 29, 100], 100) == 6
        assert bs.binarySearch([23], 23) == 0
        assert bs.binarySearch([-3, 0, 3, 6, 9, 10, 12, 50, 55, 69], 3) == 2
        assert bs.binarySearch([2, 6, 10], 23) == None
