def binarySearch(inputList, item):
        left = 0
        right = len(inputList) - 1

        while (left <= right):
                middle = (left + right) // 2
                guess = inputList[middle]

                if (guess == item):
                        return middle
                elif (guess < item):
                        left =  middle + 1
                else:
                        right = middle - 1
        # not found
        return None
