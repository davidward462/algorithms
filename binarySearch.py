def binarySearch(data, item):

        # start of the list
        low = 0
        # end of the list
        high = len(data) - 1

        while (low <= high):

                # check the middle element
                mid = (low + high) // 2 # rounded down
                guess = data[mid]

                if (guess == item):
                        # found
                        return mid
                elif (guess > item):
                        # too high
                        high = mid - 1
                else:
                        # too low
                        low = mid + 1
        # if pointers meet or pass, we did not find the item
        return None
