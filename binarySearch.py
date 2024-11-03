import pytest

def binarySearch(data, item):

        # start of the list
        low = 0
        # end of the list
        high = len(data) - 1

        while (low <= high):

                # check the middle element
                mid = (low + high) / 2 # rounded down
                guess = data[mid]
                if (guess == item):
                        # found
                        return mid
                if (guess > item):
                        # too high
                        high = mid - 1
                if (guess > item):
                        # too low
                        low = mid + 1
                return None

def test_binarySearch():
        assert binarySearch([1, 2, 3, 4, 6, 29, 100], 100) == 6
        assert binarySearch([23], 23) == 0
        assert binarySearch([-3, 0, 3, 6, 9, 10, 12, 50, 55, 69], 3) == 2
