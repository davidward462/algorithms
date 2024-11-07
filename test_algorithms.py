import pytest
import binarySearch as bs
import selectionSort as ss
import recursion as r
import quicksort as qs

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
